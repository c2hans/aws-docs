---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RdsDbUserDetails.html
---

# RdsDbUserDetails
<a name="API_RdsDbUserDetails"></a>

Contains information about the user and authentication details for a database instance involved in the finding.

## Contents
<a name="API_RdsDbUserDetails_Contents"></a>

 ** application **   <a name="guardduty-Type-RdsDbUserDetails-application"></a>
The application name used in the anomalous login attempt.
Type: String
Required: No

 ** authMethod **   <a name="guardduty-Type-RdsDbUserDetails-authMethod"></a>
The authentication method used by the user involved in the finding.
Type: String
Required: No

 ** database **   <a name="guardduty-Type-RdsDbUserDetails-database"></a>
The name of the database instance involved in the anomalous login attempt.
Type: String
Required: No

 ** ssl **   <a name="guardduty-Type-RdsDbUserDetails-ssl"></a>
The version of the Secure Socket Layer (SSL) used for the network.
Type: String
Required: No

 ** user **   <a name="guardduty-Type-RdsDbUserDetails-user"></a>
The user name used in the anomalous login attempt.
Type: String
Required: No

## See Also
<a name="API_RdsDbUserDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RdsDbUserDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RdsDbUserDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RdsDbUserDetails)
