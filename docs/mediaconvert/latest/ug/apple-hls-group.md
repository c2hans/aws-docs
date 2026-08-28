---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/apple-hls-group.html
---

# Apple HLS group
<a name="apple-hls-group"></a>

The following is an Amazon EventBridge sample event for a job with a `COMPLETE` status. It includes output file path information for an Apple HLS group.

```
{
    "detail": {
        "status": "COMPLETE",
        "paddingInserted": 0,
        "blackVideoDetected": 10,
        "blackSegments": [
            {
                "start": 0,
                "end": 10
            }
        ],
        "outputGroupDetails": [
            {
                "outputDetails": [
                    {
                        "outputFilePaths": [
                            "s3://amzn-s3-demo-bucket/hls/mainv2.m3u8"
                        ],
                        "durationInMs": 180041,
                        "blackVideoDurationInMs": 0,
                        "videoDetails": {
                            "widthInPx": 426,
                            "heightInPx": 240,
                            "averageQVBRScore": 7.38,
                            "minimumQVBRScore": 7,
                            "maximumQVBRScore": 8,
                            "minimumQVBRScoreLocationInMs": 2168,
                            "maximumQVBRScoreLocationInMs": 25025
                        }
                    },
                    {
                        "outputFilePaths": [
                            "s3://amzn-s3-demo-bucket/hls/mainv1.m3u8"
                        ],
                        "durationInMs": 180041,
                        "blackVideoDurationInMs": 0,
                        "videoDetails": {
                            "widthInPx": 1280,
                            "heightInPx": 720,
                            "averageQVBRScore": 7.38,
                            "minimumQVBRScore": 7,
                            "maximumQVBRScore": 8,
                            "minimumQVBRScoreLocationInMs": 2168,
                            "maximumQVBRScoreLocationInMs": 25025
                        }
                    }
                ],
                "type": "HLS_GROUP",
                "playlistFilePaths": [
                    "s3://amzn-s3-demo-bucket/hls/main.m3u8"
                ]
            }
        ],
        "timestamp": 1536964380391,
        "accountId": "111122223333",
        "queue": "arn:aws:mediaconvert:us-west-2:111122223333:queues/Default",
        "jobId": "1536964333549-opn151",
        "userMetadata": {},
        "warnings": [
            {
                "code": 000000,
                "count": 1
            }
        ]
    },
    "version": "0",
    "id": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "detail-type": "MediaConvert Job State Change",
    "source": "aws.mediaconvert",
    "account": "111122223333",
    "time": "2018-09-14T21:54:31Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:mediaconvert:us-west-2:111122223333:jobs/1536961999428-kxngbl"
    ]
}
```

**Note**
Quality-Defined Variable Bitrate (QVBR) statistics are only available when your video output uses QVBR rate control.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
