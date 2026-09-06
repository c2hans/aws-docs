---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ConnectorArnFilter.html
---

# ConnectorArnFilter
<a name="API_ConnectorArnFilter"></a>

A filter that matches connectors by connector ARN.

## Contents
<a name="API_ConnectorArnFilter_Contents"></a>

 ** comparison **   <a name="inspector2-Type-ConnectorArnFilter-comparison"></a>
The comparison operator for the connector ARN filter.
Type: String
Valid Values: `EQUALS`
Required: Yes

 ** value **   <a name="inspector2-Type-ConnectorArnFilter-value"></a>
The connector ARN value to filter by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws(-[a-z]+)*:inspector2:[a-z0-9-]+:[0-9]{12}:connector/([a-f0-9-]+|aws-service-connector/.+/[a-f0-9-]+)`
Required: Yes

## See Also
<a name="API_ConnectorArnFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ConnectorArnFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ConnectorArnFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ConnectorArnFilter)
