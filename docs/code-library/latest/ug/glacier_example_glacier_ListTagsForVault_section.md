---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/glacier_example_glacier_ListTagsForVault_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListTagsForVault` with an AWS SDK or CLI
<a name="glacier_example_glacier_ListTagsForVault_section"></a>

The following code examples show how to use `ListTagsForVault`.

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Glacier#code-examples).

```
    /// <summary>
    /// List tags for an Amazon S3 Glacier vault.
    /// </summary>
    /// <param name="vaultName">The name of the vault to list tags for.</param>
    /// <returns>A dictionary listing the tags attached to each object in the
    /// vault and its tags.</returns>
    public async Task<Dictionary<string, string>> ListTagsForVaultAsync(string vaultName)
    {
        var request = new ListTagsForVaultRequest
        {
            // Using a hyphen "-" for the Account Id will
            // cause the SDK to use the Account Id associated
            // with the default user.
            AccountId = "-",
            VaultName = vaultName,
        };

        var response = await _glacierService.ListTagsForVaultAsync(request);

        return response.Tags;
    }
```
+  For API details, see [ListTagsForVault](https://docs.aws.amazon.com/goto/DotNetSDKV3/glacier-2012-06-01/ListTagsForVault) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
The following command lists the tags applied to a vault named `my-vault`:

```
aws glacier list{{-}}tags-for-vault --account-id - --vault-name {{my-vault}}
```
Output:

```
{
    "Tags": {
        "date": "july2015",
        "id": "1234"
    }
}
```
Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account.
+  For API details, see [ListTagsForVault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-tags-for-vault.html) in *AWS CLI Command Reference*.

------
