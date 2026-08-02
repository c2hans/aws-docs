---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_kinesis_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# Kinesis examples using Tools for PowerShell V5
<a name="powershell_kinesis_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with Kinesis.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-KINRecord`
<a name="kinesis_GetRecords_powershell_topic"></a>

The following code example shows how to use `Get-KINRecord`.

**Tools for PowerShell V5**
**Example 1: This example shows how to return and extract data from a series of one or more records. The iterator supplierd to Get-KINRecord determines the starting position of the records to return which in this example are captured into a variable, $records. Each individual record can then be accessed by indexing the $records collection. Assuming the data in the record is UTF-8 encoded text, the final command shows how you can extract the data from the MemoryStream in the object and return it as text to the console.**

```
$records
$records = Get-KINRecord -ShardIterator "AAAAAAAAAAGIc....9VnbiRNaP"
```
**Output:**

```
MillisBehindLatest NextShardIterator            Records
------------------ -----------------            -------
0                  AAAAAAAAAAERNIq...uDn11HuUs  {Key1, Key2}
```

```
$records.Records[0]
```
**Output:**

```
ApproximateArrivalTimestamp Data                   PartitionKey SequenceNumber
--------------------------- ----                   ------------ --------------
3/7/2016 5:14:33 PM         System.IO.MemoryStream Key1         4955986459776...931586
```

```
[Text.Encoding]::UTF8.GetString($records.Records[0].Data.ToArray())
```
**Output:**

```
test data from string
```
+  For API details, see [GetRecords](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-KINShardIterator`
<a name="kinesis_GetShardIterator_powershell_topic"></a>

The following code example shows how to use `Get-KINShardIterator`.

**Tools for PowerShell V5**
**Example 1: Returns a shard iterator for the specified shard and starting position. Details of the shard identifiers and sequence numbers can be obtained from the output of the Get-KINStream cmdlet, by referencing the Shards collection of the returned stream object. The returned iterator can be used with the Get-KINRecord cmdlet to pull data records in the shard.**

```
Get-KINShardIterator -StreamName "mystream" -ShardId "shardId-000000000000" -ShardIteratorType AT_SEQUENCE_NUMBER -StartingSequenceNumber "495598645..."
```
**Output:**

```
AAAAAAAAAAGIc....9VnbiRNaP
```
+  For API details, see [GetShardIterator](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-KINStream`
<a name="kinesis_DescribeStream_powershell_topic"></a>

The following code example shows how to use `Get-KINStream`.

**Tools for PowerShell V5**
**Example 1: Returns details of the specified stream.**

```
Get-KINStream -StreamName "mystream"
```
**Output:**

```
HasMoreShards        : False
RetentionPeriodHours : 24
Shards               : {}
StreamARN            : arn:aws:kinesis:us-west-2:123456789012:stream/mystream
StreamName           : mystream
StreamStatus         : ACTIVE
```
+  For API details, see [DescribeStream](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-KINStream`
<a name="kinesis_CreateStream_powershell_topic"></a>

The following code example shows how to use `New-KINStream`.

**Tools for PowerShell V5**
**Example 1: Creates a new stream.**

```
New-KINStream -StreamName "mystream" -ShardCount 1
```
+  For API details, see [CreateStream](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-KINStream`
<a name="kinesis_DeleteStream_powershell_topic"></a>

The following code example shows how to use `Remove-KINStream`.

**Tools for PowerShell V5**
**Example 1: Deletes the specified stream. You are prompted for confirmation before the command executes. To suppress confirmation prompting use the -Force switch.**

```
Remove-KINStream -StreamName "mystream"
```
+  For API details, see [DeleteStream](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-KINRecord`
<a name="kinesis_PutRecord_powershell_topic"></a>

The following code example shows how to use `Write-KINRecord`.

**Tools for PowerShell V5**
**Example 1: Writes a record containing the string supplied to the -Text parameter.**

```
Write-KINRecord -Text "test data from string" -StreamName "mystream" -PartitionKey "Key1"
```
**Example 2: Writes a record containing the data contained in the specified file. The file is treated as a sequence of bytes so if it contains text, it should be written with any necessary encoding before using it with this cmdlet.**

```
Write-KINRecord -FilePath "C:\TestData.txt" -StreamName "mystream" -PartitionKey "Key2"
```
+  For API details, see [PutRecord](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
