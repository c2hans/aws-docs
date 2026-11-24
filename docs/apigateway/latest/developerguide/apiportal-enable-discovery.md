---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal-enable-discovery.html
---

# Enable API discovery in API Portal

You configure discovery once, and it then runs continuously. Discovery has two scopes:
+ **Single account** discovers the APIs in the current AWS account. It requires no AWS Organizations setup.
+ **AWS Organization** discovers the APIs in every account in your organization. It requires trusted access for API Portal, which only the management account can enable. After trusted access is enabled, the management account or a registered delegated administrator account can enable and manage organization-wide discovery. A delegated administrator can't delete the organization discovery configuration, and can't view or change its tags, because that configuration belongs to the management account.

Enabling discovery for a single account takes a few minutes. For an organization, API Portal enables discovery account by account, so the time scales with the number of accounts; for an organization with thousands of accounts, allow a few hours. Discovered APIs appear in the inventory as discovery runs; allow time for newly created APIs, or APIs that have recently started receiving traffic, to appear.

## Considerations
<a name="apiportal-enable-discovery-considerations"></a>

The following considerations might impact how you enable discovery:
+ Discovery is read-only. It doesn't change your APIs.
+ Discovery is Regional. Enable it in each Region where you have APIs. APIs fronted by CloudFront are discovered only in the us-east-1 Region.
+ Application Load Balancer and CloudFront APIs are discovered from traffic. An endpoint that receives no requests doesn't appear in the inventory. API Gateway APIs are discovered from their configuration and appear whether or not they receive requests, with one exception: a method defined as `ANY` or a resource that uses a `{proxy+}` path isn't expanded from configuration. API Portal creates those discovered APIs from traffic, using the actual method and path of each request it observes.
+ Discovery creates a service-linked AWS Config configuration recorder for API Portal in each account and Region where you enable it. The recorder is owned by API Portal; there is no AWS Config charge for it. You can't delete the recorder directly. To remove it, delete your discovery configuration, and API Portal deletes the recorder. AWS Config configuration items are what API Portal reads to discover API Gateway REST APIs from their configuration (without traffic) and to evaluate security posture.
+ You can exclude specific Application Load Balancer or CloudFront resources from discovery at either scope. For organization scope, you can also exclude organizational units and accounts, or include only specific organizational units and accounts. You can use exclusion filters or inclusion filters, but not both.

## Enable discovery for a single account
<a name="apiportal-enable-discovery-account"></a>

The following procedure shows how to enable discovery for the current account.

**To enable discovery for a single account**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. In the main navigation pane, under **API Portal**, choose **API inventory**.

1. Choose **Enable discovery**.

1. Under **Select scope**, choose **Single account**.

1. Under **Select services to discover**, select the services to scan: **API Gateway**, **Application Load Balancer (ALB)**, and **CloudFront**. **CloudFront** is available only in the us-east-1 Region.

1. (Optional) Under **Exclusions**, enter the ARN of an Application Load Balancer or CloudFront resource to exclude, and click **Add ARN**. Repeat for each resource that you want to exclude. You can't exclude individual API Gateway REST APIs; to leave them out, don't select **API Gateway** as a service to discover.

1. (Optional) To identify AI-facing endpoints, select **AI discovery**. See [Identify AI-facing endpoints with API Portal](apiportal-ai-discovery.md).

1. Choose **Enable discovery**.

The **API inventory** page shows **Discovery status** as **Enabled**, and discovered APIs appear as discovery runs. To change the configuration later, choose **Discovery settings**.

## Enable discovery for your AWS Organization
<a name="apiportal-enable-discovery-organization"></a>

Organization scope discovers APIs across all accounts in your AWS Organizations organization. It requires trusted access, which authorizes API Portal to read your organization's hierarchy. For more information about trusted access, see [Using AWS Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html).

**Step 1: Enable trusted access**

1. Sign in to the API Gateway console with the management account of your organization.

1. In the main navigation pane, under **API Portal**, choose **Organization settings**.

1. Under **Trusted access**, click **Enable trusted access**.

1. In the confirmation dialog, review the statement and choose **Enable trusted access**.

1. Wait until **Trusted access** shows **Enabled**. This can take several minutes.

**Step 2: (Optional) Register a delegated administrator**

Register a member account as a delegated administrator to let it manage discovery on behalf of the organization. You must enable trusted access first.

1. On the **Organization settings** page, under **Delegated administrators**, click **Register delegated administrator**.

1. Under **AWS accounts**, choose the member accounts to register, and then choose **Register delegated administrator**.

To remove a delegated administrator, select it and click **Deregister**. The account loses its ability to administer API Portal across your organization. You can register it again later.

**Step 3: Enable discovery at organization scope**

1. Under **API Portal**, choose **API inventory**, and then choose **Enable discovery**.

1. Under **Select scope**, choose **AWS Organization**.

1. Select the services to discover. **CloudFront** is available only in the us-east-1 Region.

1. (Optional) Under **Discovery filters**, either exclude organizational units, accounts, and Application Load Balancer or CloudFront resources, or include only specific organizational units and accounts.

1. (Optional) Select **AI discovery**.

1. Choose **Enable discovery**.

**Note**
If you choose **AWS Organization** scope before trusted access is enabled, the page shows the message **Trusted access is not enabled** with an **Enable trusted access** button. You can enable trusted access from there.

## Enable discovery using the AWS CLI
<a name="apiportal-enable-discovery-cli"></a>

The following command enables discovery for the current account for all three source services, with AI endpoint identification turned on.

```
aws apiportal put-discovery-configuration \
    --discovery-sources API_GATEWAY ELB CLOUDFRONT \
    --features AI_DISCOVERY \
    --region us-east-1
```

The following command enables discovery for your organization from the management account, excluding one organizational unit.

```
aws apiportal put-organization-discovery-configuration \
    --discovery-sources API_GATEWAY ELB CLOUDFRONT \
    --discovery-filters '{"exclusionFilters":{"organizationalUnitIds":["ou-{{examp-1a2b3c4d}}"]}}' \
    --region us-east-1
```

To check discovery status for each source service, run the following command. The status is `PROVISIONING`, `RUNNING`, `STOPPED`, or `FAILED`; a `FAILED` status includes a failure reason.

```
aws apiportal list-discovery-statuses --region us-east-1
```

**Note**
While organization-scope discovery is running, member accounts can't enable account-scope discovery, unless you exclude the account from organization discovery.

When you stop discovery, your inventory, managed APIs, and documentation portals remain but stop updating: new APIs aren't discovered, security findings aren't refreshed, and API reference pages in your documentation portals keep serving their last published version. Discovered APIs that you haven't added to your managed APIs are removed from the inventory about 30 days after you stop discovery; managed APIs remain until you delete them. Discovery is metered daily on the APIs in your inventory, so discovery charges continue until those APIs are removed. Documentation portal charges continue until you delete the portal.

To pause discovery without deleting the configuration, run `aws apiportal stop-discovery`. To resume, run `aws apiportal start-discovery`.

## Next steps
<a name="apiportal-enable-discovery-next-steps"></a>

After discovery is running, you can do the following:
+ Review the inventory and promote APIs to managed APIs. See [The API inventory in API Portal](apiportal-inventory.md).
+ Review the security posture of your managed APIs. See [Review security posture in API Portal](apiportal-security-posture.md).
+ Group managed APIs into a product and publish a documentation portal. See [Products in API Portal](apiportal-products.md).
