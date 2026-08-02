---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_LoginAttribute.html
---

# LoginAttribute
<a name="API_LoginAttribute"></a>

Information about the login attempts.

## Contents
<a name="API_LoginAttribute_Contents"></a>

 ** application **   <a name="guardduty-Type-LoginAttribute-application"></a>
Indicates the application name used to attempt log in.
Type: String
Required: No

 ** failedLoginAttempts **   <a name="guardduty-Type-LoginAttribute-failedLoginAttempts"></a>
Represents the sum of failed (unsuccessful) login attempts made to establish a connection to the database instance.
Type: Integer
Required: No

 ** successfulLoginAttempts **   <a name="guardduty-Type-LoginAttribute-successfulLoginAttempts"></a>
Represents the sum of successful connections (a correct combination of login attributes) made to the database instance by the actor.
Type: Integer
Required: No

 ** user **   <a name="guardduty-Type-LoginAttribute-user"></a>
Indicates the user name which attempted to log in.
Type: String
Required: No

## See Also
<a name="API_LoginAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/LoginAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/LoginAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/LoginAttribute)
