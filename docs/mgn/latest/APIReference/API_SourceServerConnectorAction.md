---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_SourceServerConnectorAction.html
---

# SourceServerConnectorAction
<a name="API_SourceServerConnectorAction"></a>

Source Server connector action.

## Contents
<a name="API_SourceServerConnectorAction_Contents"></a>

 ** connectorArn **   <a name="mgn-Type-SourceServerConnectorAction-connectorArn"></a>
Source Server connector action connector arn.
Type: String
Length Constraints: Minimum length of 27. Maximum length of 100.
Pattern: `arn:[\w-]+:mgn:([a-z]{2}-(gov-)?[a-z]+-\d{1})?:(\d{12})?:connector\/(connector-[0-9a-zA-Z]{17})`
Required: No

 ** credentialsSecretArn **   <a name="mgn-Type-SourceServerConnectorAction-credentialsSecretArn"></a>
Source Server connector action credentials secret arn.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 256.
Pattern: `arn:[\w-]+:secretsmanager:([a-z]{2}-(gov-)?[a-z]+-\d{1})?:(\d{12})?:secret:(.+)`
Required: No

## See Also
<a name="API_SourceServerConnectorAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/SourceServerConnectorAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/SourceServerConnectorAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/SourceServerConnectorAction)
