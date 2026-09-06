---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/glacier_example_glacier_AddTagsToVault_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `AddTagsToVault` with an AWS SDK or CLI
<a name="glacier_example_glacier_AddTagsToVault_section"></a>

The following code examples show how to use `AddTagsToVault`.

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Glacier#code-examples).

```
    /// <summary>
    /// Add tags to the items in an Amazon S3 Glacier vault.
    /// </summary>
    /// <param name="vaultName">The name of the vault to add tags to.</param>
    /// <param name="key">The name of the object to tag.</param>
    /// <param name="value">The tag value to add.</param>
    /// <returns>A Boolean value indicating the success of the action.</returns>
    public async Task<bool> AddTagsToVaultAsync(string vaultName, string key, string value)
    {
        var request = new AddTagsToVaultRequest
        {
            Tags = new Dictionary<string, string>
                {
                    { key, value },
                },
            AccountId = "-",
            VaultName = vaultName,
        };

        var response = await _glacierService.AddTagsToVaultAsync(request);
        return response.HttpStatusCode == HttpStatusCode.NoContent;
    }
```
+  For API details, see [AddTagsToVault](https://docs.aws.amazon.com/goto/DotNetSDKV3/glacier-2012-06-01/AddTagsToVault) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
The following command adds two tags to a vault named `my-vault`:

```
aws glacier add{{-}}tags-to-vault --account-id - --vault-name {{my-vault}} --tags {{id=1234,date=july2015}}
```
Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account.
+  For API details, see [AddTagsToVault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/add-tags-to-vault.html) in *AWS CLI Command Reference*.

------
