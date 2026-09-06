---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/organizations_example_organizations_DeleteOrganizationalUnit_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteOrganizationalUnit` with an AWS SDK or CLI
<a name="organizations_example_organizations_DeleteOrganizationalUnit_section"></a>

The following code examples show how to use `DeleteOrganizationalUnit`.

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
    /// Shows how to delete an existing AWS Organizations organizational unit.
    /// </summary>
    public class DeleteOrganizationalUnit
    {
        /// <summary>
        /// Initializes the Organizations client object and calls
        /// DeleteOrganizationalUnitAsync to delete the organizational unit
        /// with the selected ID.
        /// </summary>
        public static async Task Main()
        {
            // Create the client object using the default account.
            IAmazonOrganizations client = new AmazonOrganizationsClient();

            var orgUnitId = "ou-0000-00000000";

            var request = new DeleteOrganizationalUnitRequest
            {
                OrganizationalUnitId = orgUnitId,
            };

            var response = await client.DeleteOrganizationalUnitAsync(request);

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine($"Successfully deleted the organizational unit with ID: {orgUnitId}.");
            }
            else
            {
                Console.WriteLine($"Could not delete the organizational unit with ID: {orgUnitId}.");
            }
        }
    }
```
+  For API details, see [DeleteOrganizationalUnit](https://docs.aws.amazon.com/goto/DotNetSDKV3/organizations-2016-11-28/DeleteOrganizationalUnit) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
**To delete an OU**
The following example shows how to delete an OU. The example assumes that you previously removed all accounts and other OUs from the OU:

```
aws organizations delete-organizational-unit --organizational-unit-id {{ou-examplerootid111-exampleouid111}}
```
+  For API details, see [DeleteOrganizationalUnit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/delete-organizational-unit.html) in *AWS CLI Command Reference*.

------
