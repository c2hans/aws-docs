---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/powershell_5_dynamodb_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# DynamoDB examples using Tools for PowerShell V5
<a name="powershell_5_dynamodb_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with DynamoDB.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-DDBIndexSchema`
<a name="dynamodb_Add-DDBIndexSchema_powershell_5_topic"></a>

The following code example shows how to use `Add-DDBIndexSchema`.

**Tools for PowerShell V5**
**Example 1: Creates an empty TableSchema object and adds a new local secondary index definition to it before writing the TableSchema object to the pipeline.**

```
$schema | Add-DDBIndexSchema -IndexName "LastPostIndex" -RangeKeyName "LastPostDateTime" -RangeKeyDataType "S" -ProjectionType "keys_only"
$schema = New-DDBTableSchema
```
**Output:**

```
AttributeSchema                             KeySchema                                   LocalSecondaryIndexSchema
---------------                             ---------                                   -------------------------
{LastPostDateTime}                          {}                                          {LastPostIndex}
```
**Example 2: Adds a new local secondary index definition to the supplied TableSchema object before writing the TableSchema object back to the pipeline. The TableSchema object can also be supplied using the -Schema parameter.**

```
New-DDBTableSchema | Add-DDBIndexSchema -IndexName "LastPostIndex" -RangeKeyName "LastPostDateTime" -RangeKeyDataType "S" -ProjectionType "keys_only"
```
**Output:**

```
AttributeSchema                             KeySchema                                   LocalSecondaryIndexSchema
---------------                             ---------                                   -------------------------
{LastPostDateTime}                          {}                                          {LastPostIndex}
```
+  For API details, see [Add-DDBIndexSchema](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Add-DDBKeySchema`
<a name="dynamodb_Add-DDBKeySchema_powershell_5_topic"></a>

The following code example shows how to use `Add-DDBKeySchema`.

**Tools for PowerShell V5**
**Example 1: Creates an empty TableSchema object and adds key and attribute definition entries to it using the specified key data before writing the TableSchema object to the pipeline. The key type is declared to be 'HASH' by default; use the -KeyType paameter with a value of 'RANGE' to declare a range key.**

```
$schema = New-DDBTableSchema
$schema | Add-DDBKeySchema -KeyName "ForumName" -KeyDataType "S"
```
**Output:**

```
AttributeSchema                             KeySchema                                   LocalSecondaryIndexSchema
---------------                             ---------                                   -------------------------
{ForumName}                                 {ForumName}                                 {}
```
**Example 2: Adds new key and attribute definition entries to the supplied TableSchema object before writing the TableSchema object to the pipeline. The key type is declared to be 'HASH' by default; use the -KeyType paameter with a value of 'RANGE' to declare a range key. The TableSchema object can also be supplied using the -Schema parameter.**

```
New-DDBTableSchema | Add-DDBKeySchema -KeyName "ForumName" -KeyDataType "S"
```
**Output:**

```
AttributeSchema                             KeySchema                                   LocalSecondaryIndexSchema
---------------                             ---------                                   -------------------------
{ForumName}                                 {ForumName}                                 {}
```
+  For API details, see [Add-DDBKeySchema](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `ConvertFrom-DDBItem`
<a name="dynamodb_ConvertFrom-DDBItem_powershell_5_topic"></a>

The following code example shows how to use `ConvertFrom-DDBItem`.

**Tools for PowerShell V5**
**Example 1: ConvertFrom-DDBItem is used to convert the result of Get-DDBItem from a hashtable of DynamoDB AttributeValues to a hashtable of common types like string and double.**

```
@{
    SongTitle = 'Somewhere Down The Road'
    Artist    = 'No One You Know'
} | ConvertTo-DDBItem

Get-DDBItem -TableName 'Music' -Key $key | ConvertFrom-DDBItem
```
**Output:**

```
Name                           Value
----                           -----
Genre                          Country
Artist                         No One You Know
Price                          1.94
CriticRating                   9
SongTitle                      Somewhere Down The Road
AlbumTitle                     Somewhat Famous
```
+  For API details, see [ConvertFrom-DDBItem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `ConvertTo-DDBItem`
<a name="dynamodb_ConvertTo-DDBItem_powershell_5_topic"></a>

The following code example shows how to use `ConvertTo-DDBItem`.

**Tools for PowerShell V5**
**Example 1: An example for converting a hashtable into a dictionary of DynamoDB attribute values.**

```
@{
    SongTitle = 'Somewhere Down The Road'
    Artist    = 'No One You Know'
} | ConvertTo-DDBItem

Key       Value
---       -----
SongTitle Amazon.DynamoDBv2.Model.AttributeValue
Artist    Amazon.DynamoDBv2.Model.AttributeValue
```
**Example 2: An example for converting a hashtable into a dictionary of DynamoDB attribute values.**

```
@{
    MyMap        = @{
        MyString = 'my string'
    }
    MyStringSet  = [System.Collections.Generic.HashSet[String]]@('my', 'string')
    MyNumericSet = [System.Collections.Generic.HashSet[Int]]@(1, 2, 3)
    MyBinarySet  = [System.Collections.Generic.HashSet[System.IO.MemoryStream]]@(
        ([IO.MemoryStream]::new([Text.Encoding]::UTF8.GetBytes('my'))),
        ([IO.MemoryStream]::new([Text.Encoding]::UTF8.GetBytes('string')))
    )
    MyList1      = @('my', 'string')
    MyList2      = [System.Collections.Generic.List[Int]]@(1, 2)
    MyList3      = [System.Collections.ArrayList]@('one', 2, $true)
} | ConvertTo-DDBItem
```
**Output:**

```
Key          Value
---          -----
MyStringSet  Amazon.DynamoDBv2.Model.AttributeValue
MyList1      Amazon.DynamoDBv2.Model.AttributeValue
MyNumericSet Amazon.DynamoDBv2.Model.AttributeValue
MyList2      Amazon.DynamoDBv2.Model.AttributeValue
MyBinarySet  Amazon.DynamoDBv2.Model.AttributeValue
MyMap        Amazon.DynamoDBv2.Model.AttributeValue
MyList3      Amazon.DynamoDBv2.Model.AttributeValue
```
+  For API details, see [ConvertTo-DDBItem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DDBBatchItem`
<a name="dynamodb_BatchGetItem_powershell_5_topic"></a>

The following code example shows how to use `Get-DDBBatchItem`.

**Tools for PowerShell V5**
**Example 1: Gets the item with the SongTitle "Somewhere Down The Road" from the DynamoDB tables 'Music' and 'Songs'.**

```
$key = @{
    SongTitle = 'Somewhere Down The Road'
    Artist = 'No One You Know'
} | ConvertTo-DDBItem

$keysAndAttributes = New-Object Amazon.DynamoDBv2.Model.KeysAndAttributes
$list = New-Object 'System.Collections.Generic.List[System.Collections.Generic.Dictionary[String, Amazon.DynamoDBv2.Model.AttributeValue]]'
$list.Add($key)
$keysAndAttributes.Keys = $list

$requestItem = @{
    'Music' = [Amazon.DynamoDBv2.Model.KeysAndAttributes]$keysAndAttributes
    'Songs' = [Amazon.DynamoDBv2.Model.KeysAndAttributes]$keysAndAttributes
}

$batchItems = Get-DDBBatchItem -RequestItem $requestItem
$batchItems.GetEnumerator() | ForEach-Object {$PSItem.Value} | ConvertFrom-DDBItem
```
**Output:**

```
Name                           Value
----                           -----
Artist                         No One You Know
SongTitle                      Somewhere Down The Road
AlbumTitle                     Somewhat Famous
CriticRating                   10
Genre                          Country
Price                          1.94
Artist                         No One You Know
SongTitle                      Somewhere Down The Road
AlbumTitle                     Somewhat Famous
CriticRating                   10
Genre                          Country
Price                          1.94
```
+  For API details, see [BatchGetItem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DDBItem`
<a name="dynamodb_GetItem_powershell_5_topic"></a>

The following code example shows how to use `Get-DDBItem`.

**Tools for PowerShell V5**
**Example 1: Returns the DynamoDB item with the partition key SongTitle and the sort key Artist.**

```
$key = @{
  SongTitle = 'Somewhere Down The Road'
  Artist = 'No One You Know'
} | ConvertTo-DDBItem

Get-DDBItem -TableName 'Music' -Key $key | ConvertFrom-DDBItem
```
**Output:**

```
Name                           Value
----                           -----
Genre                          Country
SongTitle                      Somewhere Down The Road
Price                          1.94
Artist                         No One You Know
CriticRating                   9
AlbumTitle                     Somewhat Famous
```
+  For API details, see [GetItem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DDBTable`
<a name="dynamodb_DescribeTable_powershell_5_topic"></a>

The following code example shows how to use `Get-DDBTable`.

**Tools for PowerShell V5**
**Example 1: Returns details of the specified table.**

```
Get-DDBTable -TableName "myTable"
```
+  For API details, see [DescribeTable](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-DDBTableList`
<a name="dynamodb_ListTables_powershell_5_topic"></a>

The following code example shows how to use `Get-DDBTableList`.

**Tools for PowerShell V5**
**Example 1: Returns details of all tables, automatically iterating until the service indicates no further tables exist.**

```
Get-DDBTableList
```
+  For API details, see [ListTables](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Invoke-DDBQuery`
<a name="dynamodb_Query_powershell_5_topic"></a>

The following code example shows how to use `Invoke-DDBQuery`.

**Tools for PowerShell V5**
**Example 1: Invokes a query that returns DynamoDB items with the specified SongTitle and Artist.**

```
$invokeDDBQuery = @{
    TableName = 'Music'
    KeyConditionExpression = ' SongTitle = :SongTitle and Artist = :Artist'
    ExpressionAttributeValues = @{
        ':SongTitle' = 'Somewhere Down The Road'
        ':Artist' = 'No One You Know'
    } | ConvertTo-DDBItem
}
Invoke-DDBQuery @invokeDDBQuery | ConvertFrom-DDBItem
```
**Output:**

```
Name                           Value
----                           -----
Genre                          Country
Artist                         No One You Know
Price                          1.94
CriticRating                   9
SongTitle                      Somewhere Down The Road
AlbumTitle                     Somewhat Famous
```
+  For API details, see [Query](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Invoke-DDBScan`
<a name="dynamodb_Scan_powershell_5_topic"></a>

The following code example shows how to use `Invoke-DDBScan`.

**Tools for PowerShell V5**
**Example 1: Returns all items in the Music table.**

```
Invoke-DDBScan -TableName 'Music' | ConvertFrom-DDBItem
```
**Output:**

```
Name                           Value
----                           -----
Genre                          Country
Artist                         No One You Know
Price                          1.94
CriticRating                   9
SongTitle                      Somewhere Down The Road
AlbumTitle                     Somewhat Famous
Genre                          Country
Artist                         No One You Know
Price                          1.98
CriticRating                   8.4
SongTitle                      My Dog Spot
AlbumTitle                     Hey Now
```
**Example 2: Returns items in the Music table with a CriticRating greater than or equal to nine.**

```
$scanFilter = @{
        CriticRating = [Amazon.DynamoDBv2.Model.Condition]@{
            AttributeValueList = @(@{N = '9'})
            ComparisonOperator = 'GE'
        }
    }
    Invoke-DDBScan -TableName 'Music' -ScanFilter $scanFilter | ConvertFrom-DDBItem
```
**Output:**

```
Name                           Value
----                           -----
Genre                          Country
Artist                         No One You Know
Price                          1.94
CriticRating                   9
SongTitle                      Somewhere Down The Road
AlbumTitle                     Somewhat Famous
```
+  For API details, see [Scan](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-DDBTable`
<a name="dynamodb_CreateTable_powershell_5_topic"></a>

The following code example shows how to use `New-DDBTable`.

**Tools for PowerShell V5**
**Example 1: This example creates a table named Thread that has a primary key consisting of 'ForumName' (key type hash) and 'Subject' (key type range). The schema used to construct the table can be piped into each cmdlet as shown or specified using the -Schema parameter.**

```
$schema = New-DDBTableSchema
$schema | Add-DDBKeySchema -KeyName "ForumName" -KeyDataType "S"
$schema | Add-DDBKeySchema -KeyName "Subject" -KeyType RANGE -KeyDataType "S"
$schema | New-DDBTable -TableName "Thread" -ReadCapacity 10 -WriteCapacity 5
```
**Output:**

```
AttributeDefinitions   : {ForumName, Subject}
TableName              : Thread
KeySchema              : {ForumName, Subject}
TableStatus            : CREATING
CreationDateTime       : 10/28/2013 4:39:49 PM
ProvisionedThroughput  : Amazon.DynamoDBv2.Model.ProvisionedThroughputDescription
TableSizeBytes         : 0
ItemCount              : 0
LocalSecondaryIndexes  : {}
```
**Example 2: This example creates a table named Thread that has a primary key consisting of 'ForumName' (key type hash) and 'Subject' (key type range). A local secondary index is also defined. The key of the local secondary index will be set automatically from the primary hash key on the table (ForumName). The schema used to construct the table can be piped into each cmdlet as shown or specified using the -Schema parameter.**

```
$schema = New-DDBTableSchema
$schema | Add-DDBKeySchema -KeyName "ForumName" -KeyDataType "S"
$schema | Add-DDBKeySchema -KeyName "Subject" -KeyDataType "S"
$schema | Add-DDBIndexSchema -IndexName "LastPostIndex" -RangeKeyName "LastPostDateTime" -RangeKeyDataType "S" -ProjectionType "keys_only"
$schema | New-DDBTable -TableName "Thread" -ReadCapacity 10 -WriteCapacity 5
```
**Output:**

```
AttributeDefinitions   : {ForumName, LastPostDateTime, Subject}
TableName              : Thread
KeySchema              : {ForumName, Subject}
TableStatus            : CREATING
CreationDateTime       : 10/28/2013 4:39:49 PM
ProvisionedThroughput  : Amazon.DynamoDBv2.Model.ProvisionedThroughputDescription
TableSizeBytes         : 0
ItemCount              : 0
LocalSecondaryIndexes  : {LastPostIndex}
```
**Example 3: This example shows how to use a single pipeline to create a table named Thread that has a primary key consisting of 'ForumName' (key type hash) and 'Subject' (key type range) and a local secondary index. The Add-DDBKeySchema and Add-DDBIndexSchema create a new TableSchema object for you if one is not supplied from the pipeline or the -Schema parameter.**

```
New-DDBTableSchema |
  Add-DDBKeySchema -KeyName "ForumName" -KeyDataType "S" |
  Add-DDBKeySchema -KeyName "Subject" -KeyDataType "S" |
  Add-DDBIndexSchema -IndexName "LastPostIndex" `
                     -RangeKeyName "LastPostDateTime" `
                     -RangeKeyDataType "S" `
                     -ProjectionType "keys_only" |
  New-DDBTable -TableName "Thread" -ReadCapacity 10 -WriteCapacity 5
```
**Output:**

```
AttributeDefinitions   : {ForumName, LastPostDateTime, Subject}
TableName              : Thread
KeySchema              : {ForumName, Subject}
TableStatus            : CREATING
CreationDateTime       : 10/28/2013 4:39:49 PM
ProvisionedThroughput  : Amazon.DynamoDBv2.Model.ProvisionedThroughputDescription
TableSizeBytes         : 0
ItemCount              : 0
LocalSecondaryIndexes  : {LastPostIndex}
```
+  For API details, see [CreateTable](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-DDBTableSchema`
<a name="dynamodb_New-DDBTableSchema_powershell_5_topic"></a>

The following code example shows how to use `New-DDBTableSchema`.

**Tools for PowerShell V5**
**Example 1: Creates an empty TableSchema object ready to accept key and index definitions for use in creating a new Amazon DynamoDB table. The returned object can be piped into the Add-DDBKeySchema, Add-DDBIndexSchema and New-DDBTable cmdlets or passed to them using the -Schema parameter on each cmdlet.**

```
New-DDBTableSchema
```
**Output:**

```
AttributeSchema                             KeySchema                                   LocalSecondaryIndexSchema
---------------                             ---------                                   -------------------------
{}                                          {}                                          {}
```
+  For API details, see [New-DDBTableSchema](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-DDBItem`
<a name="dynamodb_DeleteItem_powershell_5_topic"></a>

The following code example shows how to use `Remove-DDBItem`.

**Tools for PowerShell V5**
**Example 1: Removes the DynamoDB item that matches the provided key.**

```
$key = @{
    SongTitle = 'Somewhere Down The Road'
    Artist = 'No One You Know'
} | ConvertTo-DDBItem
Remove-DDBItem -TableName 'Music' -Key $key -Confirm:$false
```
+  For API details, see [DeleteItem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-DDBTable`
<a name="dynamodb_DeleteTable_powershell_5_topic"></a>

The following code example shows how to use `Remove-DDBTable`.

**Tools for PowerShell V5**
**Example 1: Deletes the specified table. You are prompted for confirmation before the operation proceeds.**

```
Remove-DDBTable -TableName "myTable"
```
**Example 2: Deletes the specified table. You are not prompted for confirmation before the operation proceeds.**

```
Remove-DDBTable -TableName "myTable" -Force
```
+  For API details, see [DeleteTable](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Set-DDBBatchItem`
<a name="dynamodb_BatchWriteItem_powershell_5_topic"></a>

The following code example shows how to use `Set-DDBBatchItem`.

**Tools for PowerShell V5**
**Example 1: Creates a new item, or replaces an existing item with a new item in the DynamoDB tables Music and Songs.**

```
$item = @{
    SongTitle = 'Somewhere Down The Road'
    Artist = 'No One You Know'
    AlbumTitle = 'Somewhat Famous'
    Price = 1.94
    Genre = 'Country'
    CriticRating = 10.0
} | ConvertTo-DDBItem

$writeRequest = New-Object Amazon.DynamoDBv2.Model.WriteRequest
$writeRequest.PutRequest = [Amazon.DynamoDBv2.Model.PutRequest]$item

$requestItem = @{
    'Music' = [Amazon.DynamoDBv2.Model.WriteRequest]($writeRequest)
    'Songs' = [Amazon.DynamoDBv2.Model.WriteRequest]($writeRequest)
}

Set-DDBBatchItem -RequestItem $requestItem
```
+  For API details, see [BatchWriteItem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Set-DDBItem`
<a name="dynamodb_PutItem_powershell_5_topic"></a>

The following code example shows how to use `Set-DDBItem`.

**Tools for PowerShell V5**
**Example 1: Creates a new item, or replaces an existing item with a new item.**

```
$item = @{
  SongTitle = 'Somewhere Down The Road'
  Artist = 'No One You Know'
        AlbumTitle = 'Somewhat Famous'
        Price = 1.94
        Genre = 'Country'
        CriticRating = 9.0
} | ConvertTo-DDBItem
Set-DDBItem -TableName 'Music' -Item $item
```
+  For API details, see [PutItem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-DDBItem`
<a name="dynamodb_UpdateItem_powershell_5_topic"></a>

The following code example shows how to use `Update-DDBItem`.

**Tools for PowerShell V5**
**Example 1: Sets the genre attribute to 'Rap' on the DynamoDB item with the partition key SongTitle and the sort key Artist.**

```
$key = @{
    SongTitle = 'Somewhere Down The Road'
    Artist = 'No One You Know'
} | ConvertTo-DDBItem

$updateDdbItem = @{
    TableName = 'Music'
    Key = $key
    UpdateExpression = 'set Genre = :val1'
    ExpressionAttributeValue = (@{
        ':val1' = ([Amazon.DynamoDBv2.Model.AttributeValue]'Rap')
    })
}
Update-DDBItem @updateDdbItem
```
**Output:**

```
Name                           Value
----                           -----
Genre                          Rap
```
+  For API details, see [UpdateItem](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-DDBTable`
<a name="dynamodb_UpdateTable_powershell_5_topic"></a>

The following code example shows how to use `Update-DDBTable`.

**Tools for PowerShell V5**
**Example 1: Updates the provisioned throughput for the given table.**

```
Update-DDBTable -TableName "myTable" -ReadCapacity 10 -WriteCapacity 5
```
+  For API details, see [UpdateTable](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
