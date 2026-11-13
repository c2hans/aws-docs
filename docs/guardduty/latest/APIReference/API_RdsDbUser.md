---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RdsDbUser.html
---

# RdsDbUser
<a name="API_RdsDbUser"></a>

Contains details about the user that logged in to an Amazon RDS database instance.

## Contents
<a name="API_RdsDbUser_Contents"></a>

 ** application **   <a name="guardduty-Type-RdsDbUser-application"></a>
The name of the application that was used to log in.
Type: String
Required: No

 ** authMethod **   <a name="guardduty-Type-RdsDbUser-authMethod"></a>
The authentication method that the user used.
Type: String
Required: No

 ** database **   <a name="guardduty-Type-RdsDbUser-database"></a>
The name of the database that the user logged in to.
Type: String
Required: No

 ** ssl **   <a name="guardduty-Type-RdsDbUser-ssl"></a>
The version of Secure Sockets Layer (SSL) that the connection used.
Type: String
Required: No

 ** user **   <a name="guardduty-Type-RdsDbUser-user"></a>
The user name that was used to log in.
Type: String
Required: No

## See Also
<a name="API_RdsDbUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RdsDbUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RdsDbUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RdsDbUser)
