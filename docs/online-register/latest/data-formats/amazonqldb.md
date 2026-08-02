---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazonqldb.html
---

# Data retrieval APIs for Amazon QLDB
<a name="amazonqldb"></a>

Amazon QLDB provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="qldb-DescribeJournalKinesisStream"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/API_DescribeJournalKinesisStream.html](https://docs.aws.amazon.com/qldb/latest/developerguide/API_DescribeJournalKinesisStream.html) | Describe information about a journal kinesis stream | Read |
| <a name="qldb-DescribeJournalS3Export"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/API_DescribeJournalS3Export.html](https://docs.aws.amazon.com/qldb/latest/developerguide/API_DescribeJournalS3Export.html) | Describe information about a journal export job | Read |
| <a name="qldb-DescribeLedger"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/API_DescribeLedger.html](https://docs.aws.amazon.com/qldb/latest/developerguide/API_DescribeLedger.html) | Describe a ledger | Read |
| <a name="qldb-GetBlock"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/API_GetBlock.html](https://docs.aws.amazon.com/qldb/latest/developerguide/API_GetBlock.html) | Retrieve a block from a ledger for a given BlockAddress | Read |
| <a name="qldb-GetDigest"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/API_GetDigest.html](https://docs.aws.amazon.com/qldb/latest/developerguide/API_GetDigest.html) | Retrieve a digest from a ledger for a given BlockAddress | Read |
| <a name="qldb-GetRevision"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/API_GetRevision.html](https://docs.aws.amazon.com/qldb/latest/developerguide/API_GetRevision.html) | Retrieve a revision for a given document ID and a given BlockAddress | Read |
| <a name="qldb-ListJournalKinesisStreamsForLedger"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListJournalKinesisStreamsForLedger.html](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListJournalKinesisStreamsForLedger.html) | List journal kinesis streams for a specified ledger | List |
| <a name="qldb-ListJournalS3Exports"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListJournalS3Exports.html](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListJournalS3Exports.html) | List journal export jobs for all ledgers | List |
| <a name="qldb-ListJournalS3ExportsForLedger"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListJournalS3ExportsForLedger.html](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListJournalS3ExportsForLedger.html) | List journal export jobs for a specified ledger | List |
| <a name="qldb-ListLedgers"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListLedgers.html](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListLedgers.html) | List existing ledgers | List |
| <a name="qldb-ListTagsForResource"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListTagsForResource.html](https://docs.aws.amazon.com/qldb/latest/developerguide/API_ListTagsForResource.html) | List tags for a resource | Read |
| <a name="qldb-PartiQLHistoryFunction"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/working.history.html](https://docs.aws.amazon.com/qldb/latest/developerguide/working.history.html) | Use the history function on a table | Read |
| <a name="qldb-PartiQLSelect"></a>[https://docs.aws.amazon.com/qldb/latest/developerguide/ql-reference.select.html](https://docs.aws.amazon.com/qldb/latest/developerguide/ql-reference.select.html) | Select documents from a table | Read |
