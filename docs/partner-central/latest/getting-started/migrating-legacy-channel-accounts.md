---
source_url: https://docs.aws.amazon.com/partner-central/latest/getting-started/migrating-legacy-channel-accounts.html
---

# Migrating legacy channel accounts
<a name="migrating-legacy-channel-accounts"></a>

This guide explains how AWS Channel Partners can migrate their existing channel end customers in partner-controlled AWS Organizations to billing transfer, enabling customers to maintain independent AWS Organizations while partners retain billing responsibility.

Channel Partners have two options to migrate existing end customer accounts to billing transfer:

## Full Organization Transfer
<a name="full-organization-transfer"></a>

Transfer your existing AWS Organization to customer ownership while maintaining billing responsibility through billing transfer. This process involves transferring root account ownership to the customer after establishing billing transfer, preserving all existing organization configurations and service integrations.

**Benefits:**
+ Maintains all existing organization configurations
+ Minimizes technical complexity and migration time
+ Preserves service dependencies and integrations

**Important Considerations:**
+ Best suited for single-tenant organizations
+ Historical billing data becomes visible to the customer
+ Partner must set up billing transfer before transferring root ownership

## Member Account Transfer
<a name="member-account-transfer"></a>

Move individual member accounts from your existing AWS Organization to a new customer-owned Organization. This process involves creating a new Organization for the customer, establishing billing transfer, then migrating member accounts.

**Benefits:**
+ Maintains billing privacy throughout migration
+ Provides flexibility in migration scheduling
+ Works for both single-tenant and multi-tenant organizations

**Important Considerations:**
+ Requires rebuilding Organization-level configurations
+ Organization-level dependencies must be identified and recreated
+ Longer migration timeline than full organization transfer

**Topics**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
