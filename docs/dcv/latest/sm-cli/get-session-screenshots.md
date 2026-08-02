---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-cli/get-session-screenshots.html
---

# get-session-screenshots
<a name="get-session-screenshots"></a>

Gets screenshots of one or more Amazon DCV sessions. Optional parameters allow specifying the maximum width and height of the screenshots.

**Topics**
+ [Synopsis](#synopsis)
+ [Options](#options)
+ [Example](#example)

## Synopsis
<a name="synopsis"></a>

```
get-session-screenshots
--session-ids {{<value>}}
--max-width {{<value>}}
--max-height {{<value>}}
```

## Options
<a name="options"></a>

**`--session-ids`**
The comma-separated list of IDs of the Amazon DCV sessions to get the screenshots from.
Type: String
Required: Yes

## Example
<a name="example"></a>

```
./dcvsm get-session-screenshots --session-ids session123 --max-width 1234 --max-height 1234
```
