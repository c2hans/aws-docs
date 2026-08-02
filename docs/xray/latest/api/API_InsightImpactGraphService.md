---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_InsightImpactGraphService.html
---

# InsightImpactGraphService
<a name="API_InsightImpactGraphService"></a>

Information about an application that processed requests, users that made requests, or downstream services, resources, and applications that an application used.

## Contents
<a name="API_InsightImpactGraphService_Contents"></a>

 ** AccountId **   <a name="xray-Type-InsightImpactGraphService-AccountId"></a>
Identifier of the AWS account in which the service runs.
Type: String
Required: No

 ** Edges **   <a name="xray-Type-InsightImpactGraphService-Edges"></a>
Connections to downstream services.
Type: Array of [InsightImpactGraphEdge](API_InsightImpactGraphEdge.md) objects
Required: No

 ** Name **   <a name="xray-Type-InsightImpactGraphService-Name"></a>
The canonical name of the service.
Type: String
Required: No

 ** Names **   <a name="xray-Type-InsightImpactGraphService-Names"></a>
A list of names for the service, including the canonical name.
Type: Array of strings
Required: No

 ** ReferenceId **   <a name="xray-Type-InsightImpactGraphService-ReferenceId"></a>
Identifier for the service. Unique within the service map.
Type: Integer
Required: No

 ** Type **   <a name="xray-Type-InsightImpactGraphService-Type"></a>
Identifier for the service. Unique within the service map.
+  AWS Resource - The type of an AWS resource. For example, AWS::EC2::Instance for an application running on Amazon EC2 or AWS::DynamoDB::Table for an Amazon DynamoDB table that the application used.
+  AWS Service - The type of an AWS service. For example, AWS::DynamoDB for downstream calls to Amazon DynamoDB that didn't target a specific table.
+  AWS Service - The type of an AWS service. For example, AWS::DynamoDB for downstream calls to Amazon DynamoDB that didn't target a specific table.
+ remote - A downstream service of indeterminate type.
Type: String
Required: No

## See Also
<a name="API_InsightImpactGraphService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/InsightImpactGraphService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/InsightImpactGraphService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/InsightImpactGraphService)
