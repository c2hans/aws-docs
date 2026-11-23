---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeGuardrail.html
---

# ChangeGuardrail

A Change Guardrail and its status. A Change Guardrail checks each change to the records in a hosted zone, and rejects the change if the check fails.

When you submit a `ChangeResourceRecordSets` request, Route 53 checks each change against every guardrail that is turned on. If a check fails, Route 53 rejects the whole request and returns an error that identifies the guardrail. If every check passes, Route 53 applies the changes.

For example, suppose that `ALIAS_TARGET_CHECK` is turned on, and an alias record points to `www.example.com`. If you try to delete `www.example.com`, Route 53 rejects the request. To delete the record, first delete or change the alias record.

## Contents
<a name="API_ChangeGuardrail_Contents"></a>

 ** Name **   <a name="Route53-Type-ChangeGuardrail-Name"></a>
The name of the guardrail. Valid values are the following:
NS\_FORMAT\_CHECK
This guardrail rejects an NS record whose value looks like a Route 53 name server but isn't one.
NS\_DELEGATION\_AUTHORITY\_CHECK
This guardrail rejects an NS record that delegates a subdomain to Route 53 name servers that don't host it.
This guardrail applies only to public hosted zones.
NS\_OCCLUSION\_CHECK
This guardrail rejects a change that leaves records under a delegated subdomain, where resolvers never use them.
ALIAS\_TARGET\_CHECK
This guardrail rejects deleting a record that an alias record in the same hosted zone points to.
ACTIVE\_RECORD\_CHECK
This guardrail rejects deleting a record that still receives DNS queries, if no other record with the same name and type remains to answer them.
ACTIVE\_DELEGATION\_CHECK
This guardrail rejects deleting the NS record for a subdomain while resolvers are still referred to it.
The tier of the hosted zone determines which guardrails it includes and which ones you can turn on.
Type: String
Valid Values: `NS_FORMAT_CHECK | NS_DELEGATION_AUTHORITY_CHECK | NS_OCCLUSION_CHECK | ALIAS_TARGET_CHECK | ACTIVE_RECORD_CHECK | ACTIVE_DELEGATION_CHECK`
Required: Yes

 ** Status **   <a name="Route53-Type-ChangeGuardrail-Status"></a>
The status of the guardrail. Valid values are the following:
ENABLED
 `ENABLED` means that the guardrail is turned on.
DISABLED
 `DISABLED` means that the guardrail is turned off.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_ChangeGuardrail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/ChangeGuardrail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/ChangeGuardrail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/ChangeGuardrail)
