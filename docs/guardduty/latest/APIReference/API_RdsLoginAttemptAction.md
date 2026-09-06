---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RdsLoginAttemptAction.html
---

# RdsLoginAttemptAction
<a name="API_RdsLoginAttemptAction"></a>

Indicates that a login attempt was made to the potentially compromised database from a remote IP address.

## Contents
<a name="API_RdsLoginAttemptAction_Contents"></a>

 ** LoginAttributes **   <a name="guardduty-Type-RdsLoginAttemptAction-LoginAttributes"></a>
Indicates the login attributes used in the login attempt.
Type: Array of [LoginAttribute](API_LoginAttribute.md) objects
Required: No

 ** remoteIpDetails **   <a name="guardduty-Type-RdsLoginAttemptAction-remoteIpDetails"></a>
Contains information about the remote IP address of the connection.
Type: [RemoteIpDetails](API_RemoteIpDetails.md) object
Required: No

## See Also
<a name="API_RdsLoginAttemptAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RdsLoginAttemptAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RdsLoginAttemptAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RdsLoginAttemptAction)
