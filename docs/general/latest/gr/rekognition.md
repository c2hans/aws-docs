---
source_url: https://docs.aws.amazon.com/general/latest/gr/rekognition.html
---

# Amazon Rekognition endpoints and quotas
<a name="rekognition"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="rekognition_region"></a>

 Amazon Rekognition API operations (excluding streaming API operations) are available at the following regions and endpoints:

| Region Name | Region | Endpoint | Protocol |
| --- | --- | --- | --- |
| US East (Ohio) | us-east-2 |  rekognition.us-east-2.amazonaws.com <br /> rekognition.us-east-2.api.aws <br /> rekognition-fips.us-east-2.amazonaws.com <br /> rekognition-fips.us-east-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS |
| US East (N. Virginia) | us-east-1 |  rekognition.us-east-1.amazonaws.com <br /> rekognition-fips.us-east-1.amazonaws.com <br /> rekognition.us-east-1.api.aws <br /> rekognition-fips.us-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS |
| US West (N. California) | us-west-1 |  rekognition.us-west-1.amazonaws.com <br /> rekognition.us-west-1.api.aws <br /> rekognition-fips.us-west-1.api.aws <br /> rekognition-fips.us-west-1.amazonaws.com  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS |
| US West (Oregon) | us-west-2 |  rekognition.us-west-2.amazonaws.com <br /> rekognition-fips.us-west-2.amazonaws.com <br /> rekognition.us-west-2.api.aws <br /> rekognition-fips.us-west-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS |
| Asia Pacific (Malaysia) | ap-southeast-5 |  rekognition.ap-southeast-5.amazonaws.com <br /> rekognition.ap-southeast-5.api.aws  | HTTPS<br />HTTPS |
| Asia Pacific (Mumbai) | ap-south-1 |  rekognition.ap-south-1.amazonaws.com <br /> rekognition.ap-south-1.api.aws  | HTTPS<br />HTTPS |
| Asia Pacific (Seoul) | ap-northeast-2 |  rekognition.ap-northeast-2.amazonaws.com <br /> rekognition.ap-northeast-2.api.aws  | HTTPS<br />HTTPS |
| Asia Pacific (Singapore) | ap-southeast-1 |  rekognition.ap-southeast-1.amazonaws.com <br /> rekognition.ap-southeast-1.api.aws  | HTTPS<br />HTTPS |
| Asia Pacific (Sydney) | ap-southeast-2 |  rekognition.ap-southeast-2.amazonaws.com <br /> rekognition.ap-southeast-2.api.aws  | HTTPS<br />HTTPS |
| Asia Pacific (Thailand) | ap-southeast-7 |  rekognition.ap-southeast-7.amazonaws.com <br /> rekognition.ap-southeast-7.api.aws  | HTTPS<br />HTTPS |
| Asia Pacific (Tokyo) | ap-northeast-1 |  rekognition.ap-northeast-1.amazonaws.com <br /> rekognition.ap-northeast-1.api.aws  | HTTPS<br />HTTPS |
| Canada (Central) | ca-central-1 |  rekognition.ca-central-1.amazonaws.com <br /> rekognition.ca-central-1.api.aws <br /> rekognition-fips.ca-central-1.amazonaws.com <br /> rekognition-fips.ca-central-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS |
| Europe (Frankfurt) | eu-central-1 |  rekognition.eu-central-1.amazonaws.com <br /> rekognition.eu-central-1.api.aws  | HTTPS<br />HTTPS |
| Europe (Ireland) | eu-west-1 |  rekognition.eu-west-1.amazonaws.com <br /> rekognition.eu-west-1.api.aws  | HTTPS<br />HTTPS |
| Europe (London) | eu-west-2 |  rekognition.eu-west-2.amazonaws.com <br /> rekognition.eu-west-2.api.aws  | HTTPS<br />HTTPS |
| Europe (Spain) | eu-south-2 |  rekognition.eu-south-2.amazonaws.com <br /> rekognition.eu-south-2.api.aws  | HTTPS<br />HTTPS |
| Israel (Tel Aviv) | il-central-1 |  rekognition.il-central-1.amazonaws.com <br /> rekognition.il-central-1.api.aws  | HTTPS<br />HTTPS |
| South America (São Paulo) | sa-east-1 |  rekognition.sa-east-1.amazonaws.com <br /> rekognition.sa-east-1.api.aws  | HTTPS<br />HTTPS |
|  AWS GovCloud (US-West) | us-gov-west-1 |  rekognition.us-gov-west-1.amazonaws.com <br /> rekognition-fips.us-gov-west-1.api.aws <br /> rekognition-fips.us-gov-west-1.amazonaws.com <br /> rekognition.us-gov-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS |

### Amazon Rekognition Streaming Endpoints
<a name="regions-streaming-service-endpoints"></a>

The Amazon Rekognition streaming API operations are available at the following regions and endpoints:

|
|
| Region Name | Region | Endpoint | Protocol |
| --- |--- |--- |--- |
| US East (N. Virginia) | us-east-1 | streaming-rekognition.us-east-1.amazonaws.com streaming-rekognition-fips.us-east-1.amazonaws.com | WSSWSS |
| US West (Oregon) | us-west-2 | streaming-rekognition.us-west-2.amazonaws.com streaming-rekognition-fips.us-west-2.amazonaws.com | WSSWSS |
| Asia Pacific (Mumbai) | ap-south-1 | streaming-rekognition.ap-south-1.amazonaws.com | WSS |
| Asia Pacific (Tokyo) | ap-northeast-1 | streaming-rekognition.ap-northeast-1.amazonaws.com | WSS |
| Europe (Ireland) | eu-west-1 | streaming-rekognition.eu-west-1.amazonaws.com  | WSS |
| South America (São Paulo) | sa-east-1 | streaming-rekognition.sa-east-1.amazonaws.com | WSS |
| Asia Pacific (Malaysia) | ap-southeast-5 | streaming-rekognition.ap-southeast-5.amazonaws.com | WSS |
| Asia Pacific (Thailand) | ap-southeast-7 | streaming-rekognition.ap-southeast-7.amazonaws.com | WSS |

**Note**
Some regions only support certain Amazon Rekognition feature or operations. See the sections below for information on these differences.

The following are differences for certain Amazon Rekognition features and AWS Regions.

### Amazon Rekognition Video streaming API
<a name="regions-streaming-video"></a>

The Amazon Rekognition Video streaming API is available in the following regions, depending on the specified Settings when creating a StreamProcessor.

Label Detection (ConnectedHome) API:
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (Oregon)
+ Asia Pacific (Mumbai)
+ Europe (Ireland)

Face Search (FaceSearch) API:
+ US East (N. Virginia)
+ US West (Oregon)
+ Asia Pacific (Tokyo)
+ Europe (Frankfurt)
+ Europe (Ireland)

### Amazon Rekognition Custom Labels
<a name="endpoints-custom-labels"></a>

Amazon Rekognition Custom Labels is available in the following Regions only.
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (Oregon)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Frankfurt)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Asia Pacific (Seoul)

### Canada (Central) Region
<a name="endpoints-ca-central-1"></a>

The Canada (Central) Region supports the following operations only.
+ [AssociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AssociateFaces.html)
+ [CompareFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CompareFaces.html)
+ [CreateCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html)
+ [DeleteCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteCollection.html)
+ [DeleteFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteFaces.html)
+ [DescribeCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeCollection.html)
+ [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html)
+ [DisassociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DisassociateFaces.html)
+ [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html)
+ [ListCollections](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListCollections.html)
+ [ListFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListFaces.html)
+ [SearchFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFaces.html)
+ [SearchFacesByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFacesByImage.html)
+ [SearchUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsers.html)
+ [SearchUsersByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsersByImage.html)
+ [CreateUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateUser.html)
+ [DeleteUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteUser.html)
+ [ListUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListUsers.html)

**Note**
These operations are only available through use of the AWS CLI or SDK, as the Canada (Central) Region doesn't currently provide a console experience for these operations.

### Israel (Tel Aviv) Region
<a name="endpoints-tlv"></a>

The Israel (Tel Aviv) Region supports only the following operations for the following features.

****

| Feature | Operations |
| --- | --- |
| Face detection | [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html) |
| Face comparison | [CompareFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CompareFaces.html) |
| Face search | [AssociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AssociateFaces.html), [CreateCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html), [CreateUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateUser.html), [DeleteCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteCollection.html), [DeleteFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteFaces.html), [DeleteUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteUser.html), [DescribeCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeCollection.html), [DisassociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DisassociateFaces.html), [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html), [ListCollections](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListCollections.html), [ListFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListFaces.html), [ListUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListUsers.html), [SearchFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFaces.html), [SearchFacesByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFacesByImage.html), [SearchUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsers.html), [SearchUsersByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsersByImage.html), [TagResource](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UntagResource.html), [ListTagsForResource](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListTagsForResource.html) |
| Label detection | [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html) |
| Moderation | [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html) |
| Text detection | [DetectText](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText.html) |

## Service quotas
<a name="limits_rekognition"></a>

The quotas listed on this page are defaults. You can request a quota increase for Amazon Rekognition using the AWS Support Center. To request a quota increase for a Amazon Rekognition Transactions Per Second (TPS) limit, follow the instructions at [Default quotas](https://docs.aws.amazon.com/rekognition/latest/dg/limits.html#changeable-quotas) in the *Amazon Rekognition Developer Guide*.

Quotas increases affect only the specific API operation for the Region in which you make the request. Other API operations and Regions are not affected.

| Resource | Default |
| --- | --- |
| Transactions per second per account for individual Amazon Rekognition Image data plane operations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html)  |
| Transactions per second per account for individual Amazon Rekognition Image data plane operations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html)  |
|  Transactions per second per account for the Amazon Rekognition Image data plane operation:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) | In each Region that Amazon Rekognition Image supports – 5 |
| Transactions per second per account for the personal protective equipment data plane operation:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) | In each Region that Amazon Rekognition Image supports – 5 |
| Transactions per second per account for individual Amazon Rekognition Image control plane operations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) | In each Region that Amazon Rekognition Image supports – 5 |
| Transactions per second per account for individual stored video start operations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) | In each Region that Amazon Rekognition Video supports – 5<br />`StartCelebrityRecognition` is not available in AWS GovCloud (US). |
| Transactions per second per account for individual Amazon Rekognition Video stored video get operations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html)  |
| Maximum number of concurrent stored video jobs per account | 20 |
| Transactions per second per account for individual bulk analysis start operations: [StartMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartMediaAnalysisJob.html)  | In each Region that Amazon Rekognition bulk analysis supports: 5 |
| Transactions per second per account for individual bulk analysis list operations: [ListMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListMediaAnalysisJob.html)  | In each Region that Amazon Rekognition bulk analysis supports: 5 |
| Transactions per second per account for individual bulk analysis get operations: [GetMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetMediaAnalysisJob.html) | In each Region that Amazon Rekognition bulk analysis supports: 20 |
| Maximum number of concurrent bulk analysis jobs per account, with regard to region: |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html)  |
| Maximum number of streaming video stream processors per account that can simultaneously exist  | In each Region that Amazon Rekognition Video supports – 10,000 |
| Maximum number of face search stream processors per account that can be processed concurrently | In each Region that Amazon Rekognition Video supports face search stream processors – 10 |
| Maximum number of label detection stream processors per account that can be processed concurrently |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html)  |
| Transactions per second per account for individual streaming video operations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) | In each Region that Amazon Rekognition Video supports – 20 |
| Transactions per second per account for stop streaming video operations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) | In each Region that Amazon Rekognition Video supports – 1 |
| Transactions per second per account for Amazon Rekognition Face Liveness API operations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html)  |
| Number of concurrent Amazon Rekognition Face Liveness sessions per account, created with [StartFaceLivenessSession](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_StartFaceLivenessSession.html).  To determine your required concurrent sessions quota, multiply the estimated session length by your estimated TPS. (Ex. 10 seconds x 5 TPS = 50).  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html)  |
| Transactions per second per account for list streaming video operations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) | In each Region that Amazon Rekognition Video supports – 5 |
| Transactions per second per account for resource tagging operations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) | In each Region that Amazon Rekognition Image supports – 10 |
| Transactions per second per account for individual Amazon Rekognition Custom Label data plane operations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) | In all Regions that Amazon Rekognition Custom Labels supports – 50  |
| Transactions per second per account for individual Amazon Rekognition Custom Labels control plane operations:[See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html) | In each Region that Amazon Rekognition Custom Labels supports – 5 |
| Maximum number of Amazon Rekognition Custom Labels projects per account. | 100 |
| Maximum number of Amazon Rekognition Custom Labels models per project. | 100 |
| Maximum number of concurrent Amazon Rekognition Custom Labels training jobs per account. |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/general/latest/gr/rekognition.html)  |
| Maximum number of concurrently running Amazon Rekognition Custom Labels models per account. | 2 |
| Maximum inference units per started model. | 5 |
| Maximum number of images per dataset. | 250,000 |

For more information, see [Guidelines and quotas in Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/limits.html) in the *Amazon Rekognition Developer Guide*.
