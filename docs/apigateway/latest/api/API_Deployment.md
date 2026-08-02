---
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_Deployment.html
---

# Deployment
<a name="API_Deployment"></a>

An immutable representation of a RestApi resource that can be called by users using Stages. A deployment must be associated with a Stage for it to be callable over the Internet.

## Contents
<a name="API_Deployment_Contents"></a>

 ** apiSummary **   <a name="apigw-Type-Deployment-apiSummary"></a>
A summary of the RestApi at the date and time that the deployment resource was created.
Type: String to string to [MethodSnapshot](API_MethodSnapshot.md) object map map
Required: No

 ** createdDate **   <a name="apigw-Type-Deployment-createdDate"></a>
The date and time that the deployment resource was created.
Type: Timestamp
Required: No

 ** description **   <a name="apigw-Type-Deployment-description"></a>
The description for the deployment resource.
Type: String
Required: No

 ** id **   <a name="apigw-Type-Deployment-id"></a>
The identifier for the deployment resource.
Type: String
Required: No

## See Also
<a name="API_Deployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/Deployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/Deployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/Deployment)
