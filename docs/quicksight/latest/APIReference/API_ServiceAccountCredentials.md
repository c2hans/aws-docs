---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ServiceAccountCredentials.html
---

# ServiceAccountCredentials
<a name="API_ServiceAccountCredentials"></a>

The service account credentials used for Google Workspace domain-wide delegation. Use this structure when you authenticate a data source connection using domain-wide delegation across your Google Workspace domain.

## Contents
<a name="API_ServiceAccountCredentials_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AdminAccountEmail **   <a name="QS-Type-ServiceAccountCredentials-AdminAccountEmail"></a>
The email address of the Google Workspace administrator account that the service account impersonates through domain-wide delegation. This field is required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ClientEmail **   <a name="QS-Type-ServiceAccountCredentials-ClientEmail"></a>
The client email address of the Google service account used for domain-wide delegation. This field is required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ServiceAccountPrivateKey **   <a name="QS-Type-ServiceAccountCredentials-ServiceAccountPrivateKey"></a>
The private key of the Google service account used for domain-wide delegation. This field is required.
Type: String
Length Constraints: Minimum length of 1600. Maximum length of 8000.
Pattern: `^-{5}BEGIN (ENCRYPTED )?PRIVATE KEY-{5}\u000D?\u000A([A-Za-z0-9/+]{64}\u000D?\u000A)*[A-Za-z0-9/+]{1,64}={0,2}\u000D?\u000A-{5}END (ENCRYPTED )?PRIVATE KEY-{5}(\u000D?\u000A)?$`
Required: Yes

## See Also
<a name="API_ServiceAccountCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ServiceAccountCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ServiceAccountCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ServiceAccountCredentials)
