---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/glacier_example_glacier_DescribeVault_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeVault` with an AWS SDK or CLI
<a name="glacier_example_glacier_DescribeVault_section"></a>

The following code examples show how to use `DescribeVault`.

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Glacier#code-examples).

```
    /// <summary>
    /// Describe an Amazon S3 Glacier vault.
    /// </summary>
    /// <param name="vaultName">The name of the vault to describe.</param>
    /// <returns>The Amazon Resource Name (ARN) of the vault.</returns>
    public async Task<string> DescribeVaultAsync(string vaultName)
    {
        var request = new DescribeVaultRequest
        {
            AccountId = "-",
            VaultName = vaultName,
        };

        var response = await _glacierService.DescribeVaultAsync(request);

        // Display the information about the vault.
        Console.WriteLine($"{response.VaultName}\tARN: {response.VaultARN}");
        Console.WriteLine($"Created on: {response.CreationDate}\tNumber of Archives: {response.NumberOfArchives}\tSize (in bytes): {response.SizeInBytes}");
        if (response.LastInventoryDate != DateTime.MinValue)
        {
            Console.WriteLine($"Last inventory: {response.LastInventoryDate}");
        }

        return response.VaultARN;
    }
```
+  For API details, see [DescribeVault](https://docs.aws.amazon.com/goto/DotNetSDKV3/glacier-2012-06-01/DescribeVault) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
**To describe a vault**
The following `describe-vault` example retrieves data about a vault named `my-vault`.

```
aws glacier describe-vault \
    --vault-name {{my-vault}} \
    {{-}}-account-id -
```
Output:

```
{
    "VaultARN": "arn:aws:glacier:us-west-2:123456789012:vaults/my-vault",
    "VaultName": "my-vault",
    "CreationDate": "2015-07-17T19:22:31.123Z",
    "LastInventoryDate": "2015-07-18T03:41:12.456Z",
    "NumberOfArchives": 1,
    "SizeInBytes": 3178496
}
```
Amazon Glacier requires an account ID argument when performing operations, but you can use a hyphen to specify the in-use account.
For more information, see [Retrieving Vault Metadata in Amazon Glacier Using the AWS Command Line Interface](https://docs.aws.amazon.com/amazonglacier/latest/dev/retrieving-vault-info-cli.html) in the *Amazon Glacier Developer Guide*.
+  For API details, see [DescribeVault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/describe-vault.html) in *AWS CLI Command Reference*.

------
