import time
import json
import math
import random
from typing import List

import numpy as np

NUM_JOINTS = 6

class UR5SensorOnlySimulator:
    def __init__(self, rate_hz=50, seed=None):
        self.rate = rate_hz
        self.dt = 1.0 / rate_hz
        self.t = 0.0
        self.rng = np.random.default_rng(seed)
        # initial joint positions (rad)
        self.joints = np.zeros(NUM_JOINTS, dtype=float)
        # joint velocities (rad/s)
        self.joint_vel = np.zeros(NUM_JOINTS, dtype=float)
        # motor current / torque bias
        self.torque_bias = self.rng.normal(scale=0.05, size=NUM_JOINTS)
        # force/torque sensor bias at tool flange
        self.ft_bias_force = self.rng.normal(scale=0.2, size=3)
        self.ft_bias_torque = self.rng.normal(scale=0.02, size=3)
        # joint temperature baseline
        self.joint_temp_base = 30.0 + self.rng.normal(scale=0.5, size=NUM_JOINTS)

    def step(self):
        # simulate joint motion: simple sinusoidal patterns
        freqs = np.linspace(0.05, 0.2, NUM_JOINTS)
        amps = np.array([0.5, 0.4, 0.3, 0.6, 0.2, 0.4])
        targets = amps * np.sin(2 * math.pi * freqs * self.t)
        accel = (targets - self.joints) * 2.0 + self.rng.normal(scale=0.01, size=NUM_JOINTS)
        self.joint_vel += accel * self.dt
        self.joints += self.joint_vel * self.dt

        # joint positions
        joint_pos = self.joints + self.rng.normal(scale=0.001, size=NUM_JOINTS)
        # joint velocities
        joint_vel_meas = self.joint_vel + self.rng.normal(scale=0.005, size=NUM_JOINTS)

        # motor current / torque estimate (simple model: proportional to velocity + bias + noise)
        # In reality torque ≈ f( current, joint model ), but here we simulate:
        torque = self.torque_bias + 0.05 * self.joint_vel + self.rng.normal(scale=0.01, size=NUM_JOINTS)

        # force/torque at flange (6-axis)
        ft_force = self.ft_bias_force + self.rng.normal(scale=0.3, size=3)
        ft_torque = self.ft_bias_torque + self.rng.normal(scale=0.01, size=3)

        # joint temperatures
        joint_temp = self.joint_temp_base + 0.01 * self.t + self.rng.normal(scale=0.02, size=NUM_JOINTS)

        sample = {
            "t": round(self.t, 6),
            "joint_position": joint_pos.tolist(),
            "joint_velocity": joint_vel_meas.tolist(),
            "joint_torque_est": torque.tolist(),
            "ft_force": ft_force.tolist(),
            "ft_torque": ft_torque.tolist(),
            "joint_temperature": joint_temp.tolist(),
        }

        self.t += self.dt
        return sample

    def run_console(self, duration=None):
        start = time.time()
        next_time = start
        try:
            while True:
                now = time.time()
                if duration and (now - start) >= duration:
                    break
                s = self.step()
                print(json.dumps(s))
                next_time += self.dt
                sleep_t = next_time - time.time()
                if sleep_t > 0:
                    time.sleep(sleep_t)
                else:
                    next_time = time.time()
        except KeyboardInterrupt:
            print("# Stopped by user")


if __name__ == "__main__":
    sim = UR5SensorOnlySimulator(rate_hz=50, seed=42)
    sim.run_console(duration=5.0)
