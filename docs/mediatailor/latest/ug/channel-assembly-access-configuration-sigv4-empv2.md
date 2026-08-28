---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-access-configuration-sigv4-empv2.html
---

# Working with SigV4 for MediaPackage Version 2
<a name="channel-assembly-access-configuration-sigv4-empv2"></a>

Signature Version 4 (SigV4) for MediaPackage v2 is a signing protocol used to authenticate requests to MediaPackage v2 over HTTP. When you use SigV4 for MediaPackage v2, MediaTailor includes a signed authorization header in the HTTP request to the MediaPackage v2 endpoint used as your origin. If the signed authorization header is valid, your origin fulfills the request. If it isn't valid, the request fails.

 For general information about SigV4 for MediaPackage v2, see the [Authenticating Requests (AWS Signature Version 4)](https://docs.aws.amazon.com/mediapackage/latest/userguide/sig-v4-authenticating-requests.html) topic in the *MediaPackage v2 API reference*.

## Requirements
<a name="channel-assembly-access-configuration-sigv4-empv2-how-to"></a>

 If you activate SigV4 for MediaPackage v2 authentication for your source location, you must meet these requirements:
+ You must allow MediaTailor to access your MediaPackage v2 endpoint by granting **mediatailor.amazonaws.com** principal access in an Origin Access Policy on the endpoint.
+ Your MediaTailor source location base URL must be a MediaPackage v2 endpoint.
+ The caller of the API must have **mediapackagev2:GetObject** IAM permissions to read all multivariant playlists referenced by the MediaTailor source packaging configurations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
