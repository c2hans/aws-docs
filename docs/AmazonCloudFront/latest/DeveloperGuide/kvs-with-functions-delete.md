---
source_url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/kvs-with-functions-delete.html
---

# Delete a key value store
<a name="kvs-with-functions-delete"></a>

You can delete your key value store by using the Amazon CloudFront console or API.

------
#### [ Console ]

**To delete a key value store**

1. Sign in to the AWS Management Console and open the **Functions** page in the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home#/functions](https://console.aws.amazon.com/cloudfront/v4/home#/functions).

1. Choose the function name.

1. Under the **Associated KeyValueStore** section, verify if a key value store is associated with the function. If it is, remove the association by choosing **Disassociate KeyValueStore** and then choose **Remove association**.

1. In the navigation pane, choose the **Functions** page and then choose the **KeyValueStores** tab.

1. Select the key value store that you want to delete and then choose **Delete**.

------
#### [ AWS CLI ]

**To delete a key value store**

1. Get the `ETag` and the name of the key value stores. For more information, see [Get a reference to a key value store](kvs-with-functions-get-reference.md).

1. Verify if the key value stores is associated with a function. If it is, remove the association. For more information on both these steps, see [Update functions](update-function.md).

1. After you have the name and `ETag` of the key value store and it's no longer associated with a function, you can delete it.

   Run the following command to delete the specified key value store.

   ```
   aws cloudfront delete-key-value-store \
       --name=keyvaluestore1 \
       --if-match=E3UN6WX5RRO2AG
   ```

------
#### [ API ]

**To delete a key value store**

1. Get the `ETag` and the name of the key value stores. For more information, see [Get a reference to a key value store](kvs-with-functions-get-reference.md).

1. Verify if the key value stores is associated with a function. If it is, remove the association. For more information on both these steps, see [Update functions](update-function.md).

1. To delete the key value store, use the CloudFront [DeleteKeyValueStore](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteKeyValueStore.html) API operation.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudFront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
