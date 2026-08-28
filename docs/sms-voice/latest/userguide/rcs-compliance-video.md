---
source_url: https://docs.aws.amazon.com/sms-voice/latest/userguide/rcs-compliance-video.html
---

# Launch video requirements
<a name="rcs-compliance-video"></a>

Country launch registrations for the United States and Canada require a screen recording (video) that demonstrates your RCS messaging experience. This is the second most common source of denials.

## What the video must show
<a name="rcs-compliance-video-content"></a>

Your launch video must demonstrate the complete end-user experience:

1. **A sample message exchange** — Show at least one example of the messages your agent sends to users. The message content must match your declared use case (transactional, promotional, or multi-use). If your agent is declared as multi-use, show at least one transactional and one promotional message.

1. **HELP keyword response** — Show a user sending the word "HELP" and receiving your configured HELP response message. The HELP response must include valid customer care contact information (email, phone number, or a working URL to a help page).

1. **STOP keyword response** — Show a user sending the word "STOP" and receiving your configured opt-out response message. The opt-out response must include your brand/program name and confirm that no further messages will be sent.

1. **Confirmation/welcome message** — Show the first message (confirmation MT) sent to a user after they opt in. This message must include your brand name and confirm the subscription. See [Opt-in confirmation message](rcs-compliance-optin.md#rcs-compliance-optin-confirmation).

1. **Use case alignment** — If your agent is declared as multi-use, the video must show both transactional AND promotional message examples. If declared as transactional, show only transactional messages.

## Video hosting requirements
<a name="rcs-compliance-video-hosting"></a>
+ The video must be hosted at a publicly accessible URL (no authentication required).
+ Direct download links are acceptable but cloud-hosted streaming URLs are preferred.
+ The URL must be functional at the time of review. Broken or expired links result in immediate denial.

## Common video denials
<a name="rcs-compliance-video-denials"></a>

| Issue | What went wrong | How to fix |
| --- | --- | --- |
| Wrong keyword | Video shows "SUPPORT" instead of "HELP" | Re-record showing the exact HELP keyword |
| Use case mismatch | Video shows only transactional messages but agent is multi-use | Include both promotional and transactional examples |
| Missing sample message | Video doesn't demonstrate actual message content | Add a section showing a realistic message exchange |
| URL not accessible | Video link is broken, expired, or behind authentication | Host on a publicly accessible URL and verify the link works |
| Opt-out mismatch | STOP response in video doesn't match agent configuration | Ensure the video shows the exact opt-out response configured on your agent |

## Tips
<a name="rcs-compliance-video-tips"></a>
+ Record the video on an actual device showing the native messaging app.
+ Keep the video concise (30-60 seconds is sufficient).
+ Ensure text is legible — avoid small screens or low resolution.
+ Test the video URL in an incognito/private browser window before submitting.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sms-voice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
