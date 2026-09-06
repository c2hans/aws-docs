---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/organizations_example_organizations_DeleteOrganization_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteOrganization` with an AWS SDK or CLI
<a name="organizations_example_organizations_DeleteOrganization_section"></a>

The following code examples show how to use `DeleteOrganization`.

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Organizations#code-examples).

```
    using System;
    using System.Threading.Tasks;
    using Amazon.Organizations;
    using Amazon.Organizations.Model;

    /// <summary>
    /// Shows how to delete an existing organization using the AWS
    /// Organizations Service.
    /// </summary>
    public class DeleteOrganization
    {
        /// <summary>
        /// Initializes the Organizations client and then calls
        /// DeleteOrganizationAsync to delete the organization.
        /// </summary>
        public static async Task Main()
        {
            // Create the client object using the default account.
            IAmazonOrganizations client = new AmazonOrganizationsClient();

            var response = await client.DeleteOrganizationAsync(new DeleteOrganizationRequest());

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine("Successfully deleted organization.");
            }
            else
            {
                Console.WriteLine("Could not delete organization.");
            }
        }
    }
```
+  For API details, see [DeleteOrganization](https://docs.aws.amazon.com/goto/DotNetSDKV3/organizations-2016-11-28/DeleteOrganization) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
**To delete an organization**
The following example shows how to delete an organization. To perform this operation, you must be an admin of the master account in the organization. The example assumes that you previously removed all the member accounts, OUs, and policies from the organization:

```
aws organizations delete-organization
```
+  For API details, see [DeleteOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-organization.html) in *AWS CLI Command Reference*.

------
