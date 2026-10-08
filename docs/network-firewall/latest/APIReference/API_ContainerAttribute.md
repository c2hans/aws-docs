---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_ContainerAttribute.html
---

# ContainerAttribute
<a name="API_ContainerAttribute"></a>

A key-value filter pair used in container association monitoring configurations to narrow which containers are tracked. The key must match exactly. The value can be an exact value or a wildcard pattern.

## Contents
<a name="API_ContainerAttribute_Contents"></a>

 ** Key **   <a name="networkfirewall-Type-ContainerAttribute-Key"></a>
The attribute key to filter on. For Amazon EKS, specify `namespace` to filter by namespace, or specify a Kubernetes label key. For Amazon ECS, specify a container instance attribute name. Keys don't support wildcards.
Valid characters are letters, numbers, spaces, hyphens (`-`), underscores (`_`), periods (`.`), forward slashes (`/`), and colons (`:`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

 ** Value **   <a name="networkfirewall-Type-ContainerAttribute-Value"></a>
The attribute value to match. You can specify an exact value, such as `payments-api`, or a wildcard pattern, such as `payments-*`.
Valid characters are letters, numbers, spaces, hyphens (`-`), underscores (`_`), periods (`.`), forward slashes (`/`), colons (`:`), asterisks (`*`), and backslashes (`\`).
Network Firewall evaluates the value using the following rules:
+ An asterisk (`*`) matches zero or more characters. For example, `payments-*` matches `payments-`, `payments-api`, and `payments-api-v2`, and `*-prod` matches `web-prod`.
+ The pattern must match the entire value. For example, `payments-*` doesn't match `my-payments-api`. To match a value that contains `payments` anywhere, use `*payments*`.
+ Matching is case sensitive. For example, `Payments-*` doesn't match `payments-api`.
+ To match a literal asterisk, escape it with a backslash (`\*`). To match a literal backslash, use `\\`. A backslash followed by any other character matches a literal backslash followed by that character.
+ A wildcard pattern matches only containers that have the attribute. For example, a filter with key `app` and value `*` matches every container that has an `app` label, but doesn't match a container without an `app` label.
+ A value that doesn't contain `*` or `\` matches only that exact value.
A value can contain at most 10 unescaped asterisks. Escaped asterisks (`\*`) don't count toward this limit. A value can't end with a single unescaped backslash.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\S+`
Required: Yes

## See Also
<a name="API_ContainerAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ContainerAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ContainerAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ContainerAttribute)
