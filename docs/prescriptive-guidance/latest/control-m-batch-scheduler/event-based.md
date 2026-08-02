---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/control-m-batch-scheduler/event-based.html
---

# Base job runs on events
<a name="event-based"></a>

Control-M Managed File Transfer (MFT) is an FTP/SFTP client and server that you can use to watch and transfer files between a local host and a remote host. For more information about defining a File Transfer job, see the [Control-M documentation](https://documents.bmc.com/supportu/9.0.21/en-US/Documentation/File_Transfer_Job.htm).

This pilot uses the File Transfer job to watch for a file-creation event of a file with the .poc extension in the `/bmcfile`  folder in an S3 bucket named `bmc-poc-bucket`. When that event occurs, the Control-M job is initiated to run the next job. You can optionally pass the full path, including the bucket name.
