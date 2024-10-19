import pywhatkit
import time

# List of phone numbers (make sure to include the country code, e.g., "+20" for Egypt)
phone_numbers = [
    "+201022425648",
    "+201027182532",
    "+201016293580",
    "+201148116649",
    "+201212483853",
    "+201060607913",
    "+201212446461",
    "+201141711354",
    "+201016293580",
    "+201020198938",
    "+201022425648",
    "+201025188021",
    "+201009718190",
    "+201017098632",
    "+201096141560"
]

# The message to send
message = """مساء الخير
اي الاخبار عامل اي 💙
اناعمرو علي   
IEEE Head of the Embedded systems Committee

أحب أبلغك إن :
- وصلك ميل عشان تحجز معاد لل interview لو مكنتش حجزته (لو حجزته فانت تمام تقدر تيجي فيه)
⁠
- مكان الانترفيو هيكون في أكاديمية الاحتراف المهني الدولية للتدريب IPA.

وده عنوان المكان: ميدان 47، خلف كازيون، اكاديميه الاحتراف المهني الدولية للتدريب IPA.

ده اللوكيشن:
https://maps.app.goo.gl/58rBpwcJ8mSZPAh16

وده لينك بيدج المكان:
https://www.facebook.com/profile.php?id=61553532031650&mibextid=ZbWKwL

هستناك 🤍💙"""

# Specify the delay between each message (in seconds)
delay_between_messages = 30

# Loop through the list and send the message to each number
for number in phone_numbers:
    try:
        # Send the message at the next minute (adjust as needed)
        pywhatkit.sendwhatmsg(number, message, time.localtime().tm_hour, time.localtime().tm_min + 2)
        
        # Wait before sending the next message to avoid spamming
        time.sleep(delay_between_messages)
    except Exception as e:
        print(f"Failed to send message to {number}: {e}")
