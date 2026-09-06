---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/built-in-intent-pause.html
---

# AMAZON.PauseIntent
<a name="built-in-intent-pause"></a>

Responds to words and phrases that enable the user to pause an interaction with a bot so that they can return to it later. Your Lambda function or application needs to save intent data in session variables, or you need to use the [GetSession](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_GetSession.html) operation to retrieve intent data when you resume the current intent.

Common utterances:
+ pause
+ pause that
