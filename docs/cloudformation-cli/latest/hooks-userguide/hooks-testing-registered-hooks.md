---
source_url: https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-testing-registered-hooks.html
---

# Testing a custom Hook for public use
<a name="hooks-testing-registered-hooks"></a>

In order to publish your registered custom Hook, it must pass all test requirements defined for it. The following is a list of requirements needed before publishing your custom Hook as a third-party extension.

Each handler and target is tested twice. Once for `SUCCESS` and once for `FAILED`.
+ For `SUCCESS` response case:
  + Status must be `SUCCESS`.
  + Must not return an error code.
  + Callback delay should be set to `0` seconds, if specified.
+ For `FAILED` response case:
  + Status must be `FAILED`.
  + Must return an error code.
  + Must have a message in response.
  + Callback delay should be set to `0` seconds, if specified.
+ For `IN_PROGRESS` response case:
  + Must not return an error code.
  + `Result` field must not be set in response.
