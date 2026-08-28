---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_Denied.html
---

# Denied
<a name="API_Denied"></a>

Contains information that denied the authorization.

## Contents
<a name="API_Denied_Contents"></a>

 ** explicitDeny **   <a name="iot-Type-Denied-explicitDeny"></a>
Information that explicitly denies the authorization.
Type: [ExplicitDeny](API_ExplicitDeny.md) object
Required: No

 ** implicitDeny **   <a name="iot-Type-Denied-implicitDeny"></a>
Information that implicitly denies the authorization. When a policy doesn't explicitly deny or allow an action on a resource it is considered an implicit deny.
Type: [ImplicitDeny](API_ImplicitDeny.md) object
Required: No

## See Also
<a name="API_Denied_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/Denied)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/Denied)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/Denied)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
