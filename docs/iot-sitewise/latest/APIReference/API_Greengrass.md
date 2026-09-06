---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Greengrass.html
---

# Greengrass
<a name="API_Greengrass"></a>

Contains details for a gateway that runs on AWS IoT Greengrass. To create a gateway that runs on AWS IoT Greengrass, you must add the IoT SiteWise connector to a Greengrass group and deploy it. Your Greengrass group must also have permissions to upload data to AWS IoT SiteWise. For more information, see [Ingesting data using a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-connector.html) in the * AWS IoT SiteWise User Guide*.

## Contents
<a name="API_Greengrass_Contents"></a>

 ** groupArn **   <a name="iotsitewise-Type-Greengrass-groupArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Greengrass group. For more information about how to find a group's ARN, see [ListGroups](https://docs.aws.amazon.com/greengrass/v1/apireference/listgroups-get.html) and [GetGroup](https://docs.aws.amazon.com/greengrass/v1/apireference/getgroup-get.html) in the * AWS IoT Greengrass V1 API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

## See Also
<a name="API_Greengrass_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/Greengrass)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/Greengrass)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/Greengrass)
