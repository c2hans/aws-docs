---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_Service.html
---

# Service
<a name="API_Service"></a>

Information about an application that processed requests, users that made requests, or downstream services, resources, and applications that an application used.

## Contents
<a name="API_Service_Contents"></a>

 ** AccountId **   <a name="xray-Type-Service-AccountId"></a>
Identifier of the AWS account in which the service runs.
Type: String
Required: No

 ** DurationHistogram **   <a name="xray-Type-Service-DurationHistogram"></a>
A histogram that maps the spread of service durations.
Type: Array of [HistogramEntry](API_HistogramEntry.md) objects
Required: No

 ** Edges **   <a name="xray-Type-Service-Edges"></a>
Connections to downstream services.
Type: Array of [Edge](API_Edge.md) objects
Required: No

 ** EndTime **   <a name="xray-Type-Service-EndTime"></a>
The end time of the last segment that the service generated.
Type: Timestamp
Required: No

 ** Name **   <a name="xray-Type-Service-Name"></a>
The canonical name of the service.
Type: String
Required: No

 ** Names **   <a name="xray-Type-Service-Names"></a>
A list of names for the service, including the canonical name.
Type: Array of strings
Required: No

 ** ReferenceId **   <a name="xray-Type-Service-ReferenceId"></a>
Identifier for the service. Unique within the service map.
Type: Integer
Required: No

 ** ResponseTimeHistogram **   <a name="xray-Type-Service-ResponseTimeHistogram"></a>
A histogram that maps the spread of service response times.
Type: Array of [HistogramEntry](API_HistogramEntry.md) objects
Required: No

 ** Root **   <a name="xray-Type-Service-Root"></a>
Indicates that the service was the first service to process a request.
Type: Boolean
Required: No

 ** StartTime **   <a name="xray-Type-Service-StartTime"></a>
The start time of the first segment that the service generated.
Type: Timestamp
Required: No

 ** State **   <a name="xray-Type-Service-State"></a>
The service's state.
Type: String
Required: No

 ** SummaryStatistics **   <a name="xray-Type-Service-SummaryStatistics"></a>
Aggregated statistics for the service.
Type: [ServiceStatistics](API_ServiceStatistics.md) object
Required: No

 ** Type **   <a name="xray-Type-Service-Type"></a>
The type of service.
+  AWS Resource - The type of an AWS resource. For example, `AWS::EC2::Instance` for an application running on Amazon EC2 or `AWS::DynamoDB::Table` for an Amazon DynamoDB table that the application used.
+  AWS Service - The type of an AWS service. For example, `AWS::DynamoDB` for downstream calls to Amazon DynamoDB that didn't target a specific table.
+  `client` - Represents the clients that sent requests to a root service.
+  `remote` - A downstream service of indeterminate type.
Type: String
Required: No

## See Also
<a name="API_Service_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/Service)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/Service)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/Service)
