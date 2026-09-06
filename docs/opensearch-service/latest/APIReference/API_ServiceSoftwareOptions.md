---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ServiceSoftwareOptions.html
---

# ServiceSoftwareOptions
<a name="API_ServiceSoftwareOptions"></a>

The current status of the service software for an Amazon OpenSearch Service domain. For more information, see [Service software updates in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/service-software.html).

## Contents
<a name="API_ServiceSoftwareOptions_Contents"></a>

 ** AutomatedUpdateDate **   <a name="opensearchservice-Type-ServiceSoftwareOptions-AutomatedUpdateDate"></a>
The timestamp, in Epoch time, until which you can manually request a service software update. After this date, we automatically update your service software.
Type: Timestamp
Required: No

 ** Cancellable **   <a name="opensearchservice-Type-ServiceSoftwareOptions-Cancellable"></a>
 True if you're able to cancel your service software version update. False if you can't cancel your service software update.
Type: Boolean
Required: No

 ** CurrentVersion **   <a name="opensearchservice-Type-ServiceSoftwareOptions-CurrentVersion"></a>
The current service software version present on the domain.
Type: String
Required: No

 ** Description **   <a name="opensearchservice-Type-ServiceSoftwareOptions-Description"></a>
A description of the service software update status.
Type: String
Required: No

 ** NewVersion **   <a name="opensearchservice-Type-ServiceSoftwareOptions-NewVersion"></a>
The new service software version, if one is available.
Type: String
Required: No

 ** OptionalDeployment **   <a name="opensearchservice-Type-ServiceSoftwareOptions-OptionalDeployment"></a>
True if a service software is never automatically updated. False if a service software is automatically updated after the automated update date.
Type: Boolean
Required: No

 ** UpdateAvailable **   <a name="opensearchservice-Type-ServiceSoftwareOptions-UpdateAvailable"></a>
True if you're able to update your service software version. False if you can't update your service software version.
Type: Boolean
Required: No

 ** UpdateStatus **   <a name="opensearchservice-Type-ServiceSoftwareOptions-UpdateStatus"></a>
The status of your service software update.
Type: String
Valid Values: `PENDING_UPDATE | IN_PROGRESS | COMPLETED | NOT_ELIGIBLE | ELIGIBLE`
Required: No

## See Also
<a name="API_ServiceSoftwareOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ServiceSoftwareOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ServiceSoftwareOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ServiceSoftwareOptions)
