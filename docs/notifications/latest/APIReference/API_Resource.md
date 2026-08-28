---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

A resource affected by or closely linked to an event.

## Contents
<a name="API_Resource_Contents"></a>

 ** arn **   <a name="Notifications-Type-Resource-arn"></a>
The Amazon Resource Name (ARN) of the resource. At least one id or ARN is required.
Type: String
Pattern: `arn:[^:]*:[^:]*:[^:]*:.*`
Required: No

 ** detailUrl **   <a name="Notifications-Type-Resource-detailUrl"></a>
The URL to the resource's detail page. If a detail page URL is unavailable, it is the URL to an informational page that describes the resource's type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Pattern: `(https?)://.*`
Required: No

 ** id **   <a name="Notifications-Type-Resource-id"></a>
The unique identifier for the resource.
At least one id or ARN is required.
Type: String
Required: No

 ** tags **   <a name="Notifications-Type-Resource-tags"></a>
A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
