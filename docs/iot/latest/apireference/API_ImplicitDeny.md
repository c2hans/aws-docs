---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ImplicitDeny.html
---

# ImplicitDeny
<a name="API_ImplicitDeny"></a>

Information that implicitly denies authorization. When policy doesn't explicitly deny or allow an action on a resource it is considered an implicit deny.

## Contents
<a name="API_ImplicitDeny_Contents"></a>

 ** policies **   <a name="iot-Type-ImplicitDeny-policies"></a>
Policies that don't contain a matching allow or deny statement for the specified action on the specified resource.
Type: Array of [Policy](API_Policy.md) objects
Required: No

## See Also
<a name="API_ImplicitDeny_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ImplicitDeny)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ImplicitDeny)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ImplicitDeny)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
