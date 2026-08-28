---
source_url: https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-connection-CNAME-delete-api.html
---

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025.

# Deleting a custom domain
<a name="connecting-connection-CNAME-delete-api"></a>

To delete the custom domain name, the user must have permissions for the following actions:
+ For a provisioned cluster: `redshift:DeleteCustomDomainAssociation`
+ For an Amazon Redshift Serverless workgroup: `redshiftServerless:DeleteCustomDomainAssociation`

**On the console**

You can delete the custom domain name by selecting the **Actions** button and choosing **Delete custom domain name**. After you do this, you can still connect to the server by updating your tools to use the endpoints listed in the console.

**Using a CLI command**

The following sample shows how to delete the custom domain name. The delete operation requires that you provide the existing custom domain name for the cluster.

```
aws redshift delete-custom-domain-association ––cluster-id {{redshiftcluster}} ––custom-domain-name {{customdomainname}}
```

The following sample shows how to delete the custom domain name for an Amazon Redshift Serverless workgroup. The custom domain name is a required parameter.

```
aws redshift-serverless delete-custom-domain-association ––workgroup-name {{workgroupname}} ––custom-domain-name {{customdomainname}}
```

For more information, see [DeleteCustomDomainAssociation](https://docs.aws.amazon.com/redshift/latest/APIReference/API_DeleteCustomDomainAssociation.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
