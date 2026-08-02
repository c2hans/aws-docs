---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotationRulesType.html
---

# RotationRulesType
<a name="API_RotationRulesType"></a>

A structure that defines the rotation configuration for the secret.

## Contents
<a name="API_RotationRulesType_Contents"></a>

 ** AutomaticallyAfterDays **   <a name="SecretsManager-Type-RotationRulesType-AutomaticallyAfterDays"></a>
The number of days between rotations of the secret. You can use this value to check that your secret meets your compliance guidelines for how often secrets must be rotated. If you use this field to set the rotation schedule, Secrets Manager calculates the next rotation date based on the previous rotation. Manually updating the secret value by calling `PutSecretValue` or `UpdateSecret` is considered a valid rotation.
In `DescribeSecret` and `ListSecrets`, this value is calculated from the rotation schedule after every successful rotation. In `RotateSecret`, you can set the rotation schedule in `RotationRules` with `AutomaticallyAfterDays` or `ScheduleExpression`, but not both. To set a rotation schedule in hours, use `ScheduleExpression`.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** Duration **   <a name="SecretsManager-Type-RotationRulesType-Duration"></a>
The length of the rotation window in hours, for example `3h` for a three hour window. Secrets Manager rotates your secret at any time during this window. The window must not extend into the next rotation window or the next UTC day. The window starts according to the `ScheduleExpression`. If you don't specify a `Duration`, for a `ScheduleExpression` in hours, the window automatically closes after one hour. For a `ScheduleExpression` in days, the window automatically closes at the end of the UTC day. For more information, including examples, see [Schedule expressions in Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_schedule.html) in the *Secrets Manager Users Guide*.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `[0-9]+h`
Required: No

 ** ScheduleExpression **   <a name="SecretsManager-Type-RotationRulesType-ScheduleExpression"></a>
A `cron()` or `rate()` expression that defines the schedule for rotating your secret. Secrets Manager rotation schedules use UTC time zone. Secrets Manager rotates your secret any time during a rotation window.
Secrets Manager `rate()` expressions represent the interval in hours or days that you want to rotate your secret, for example `rate(12 hours)` or `rate(10 days)`. You can rotate a secret as often as every four hours. If you use a `rate()` expression, the rotation window starts at midnight. For a rate in hours, the default rotation window closes after one hour. For a rate in days, the default rotation window closes at the end of the day. You can set the `Duration` to change the rotation window. The rotation window must not extend into the next UTC day or into the next rotation window.
You can use a `cron()` expression to create a rotation schedule that is more detailed than a rotation interval. For more information, including examples, see [Schedule expressions in Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_schedule.html) in the *Secrets Manager Users Guide*. For a cron expression that represents a schedule in hours, the default rotation window closes after one hour. For a cron expression that represents a schedule in days, the default rotation window closes at the end of the day. You can set the `Duration` to change the rotation window. The rotation window must not extend into the next UTC day or into the next rotation window.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z\(\)#\?\*\-\/, ]+`
Required: No

## See Also
<a name="API_RotationRulesType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/RotationRulesType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/RotationRulesType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/RotationRulesType)
