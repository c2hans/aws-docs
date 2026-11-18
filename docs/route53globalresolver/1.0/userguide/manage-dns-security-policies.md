---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/manage-dns-security-policies.html
---

# Manage DNS security policies in Amazon Route 53 Global Resolver
<a name="manage-dns-security-policies"></a>

## Managing global resolvers
<a name="managing-resolvers"></a>

After creating a global resolver, you can view its details, edit its configuration, and manage associated resources from the Global Resolvers page.

### Viewing resolver details
<a name="viewing-resolver-details"></a>

The Global Resolvers page displays a list of all your resolvers with key information including resolver name, deployed regions, associated DNS views, observability region, and operational status.

### Editing global resolvers
<a name="editing-resolvers"></a>

You can modify the resolver name and description after creation. You cannot modify the regions where a global resolver is deployed after creation.

## Managing firewall rules
<a name="managing-firewall-rules"></a>

After creating firewall rules, you can modify their priority, update their configuration, or delete them as needed.

### Rule priority and evaluation order
<a name="rule-priority"></a>

Firewall rules are evaluated in priority order, with lower numbers processed first. When a query matches multiple rules, only the first matching rule's action is applied.

### Updating firewall rules
<a name="updating-rules"></a>

You can update most aspects of a firewall rule after creation, including its priority, action, and target domains.
