---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PortalSummary.html
---

# PortalSummary
<a name="API_PortalSummary"></a>

Contains a portal summary.

## Contents
<a name="API_PortalSummary_Contents"></a>

 ** id **   <a name="iotsitewise-Type-PortalSummary-id"></a>
The ID of the portal.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** name **   <a name="iotsitewise-Type-PortalSummary-name"></a>
The name of the portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** startUrl **   <a name="iotsitewise-Type-PortalSummary-startUrl"></a>
The URL for the AWS IoT SiteWise Monitor portal. You can use this URL to access portals that use IAM Identity Center for authentication. For portals that use IAM for authentication, you must use the AWS IoT SiteWise console to get a URL that you can use to access the portal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^(http|https)\://\S+`
Required: Yes

 ** status **   <a name="iotsitewise-Type-PortalSummary-status"></a>
Contains information about the current status of a portal.
Type: [PortalStatus](API_PortalStatus.md) object
Required: Yes

 ** creationDate **   <a name="iotsitewise-Type-PortalSummary-creationDate"></a>
The date the portal was created, in Unix epoch time.
Type: Timestamp
Required: No

 ** description **   <a name="iotsitewise-Type-PortalSummary-description"></a>
The portal's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** lastUpdateDate **   <a name="iotsitewise-Type-PortalSummary-lastUpdateDate"></a>
The date the portal was last updated, in Unix epoch time.
Type: Timestamp
Required: No

 ** portalType **   <a name="iotsitewise-Type-PortalSummary-portalType"></a>
Define the type of portal. The value for AWS IoT SiteWise Monitor (Classic) is `SITEWISE_PORTAL_V1`. The value for AWS IoT SiteWise Monitor (AI-aware) is `SITEWISE_PORTAL_V2`.
Type: String
Valid Values: `SITEWISE_PORTAL_V1 | SITEWISE_PORTAL_V2`
Required: No

 ** roleArn **   <a name="iotsitewise-Type-PortalSummary-roleArn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the service role that allows the portal's users to access your AWS IoT SiteWise resources on your behalf. For more information, see [Using service roles for AWS IoT SiteWise Monitor](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html) in the * AWS IoT SiteWise User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.\+=,@]+$`
Required: No

## See Also
<a name="API_PortalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/PortalSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/PortalSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/PortalSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
