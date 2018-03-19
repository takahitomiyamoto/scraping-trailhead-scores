# scraping-trailhead-scores

You can get the data of trailhead scores as tsv-style.

## clone
    git clone https://github.com/takahitomiyamoto/scraping-trailhead-scores.git
    cd scraping-trailhead-scores

## prepare data (data/trailhead_users.csv)

### Format:

|1|2|
|:---|:---|
|User Name|User ID|

- User Name : only used as a label
- User ID : [https://trailhead.salesforce.com/en/me/<u>**User ID**</u>]()

### Example:

```data/trailhead_users.csv
@takahito0508,takahito0508
Taro Yamada,005XXXXXXXXXXXXXXX
```

## execute
    sudo chmod +x ./scrapingTrailheadScores.sh
    ./scrapingTrailheadScores.sh

## check result (result/trailhead_scores.tsv)

### Format:

|1|2|3|4|5|6|
|:---|:---|:---|:---|:---|:---|
|User Name|User ID|Badges|Points|Trails Completed|Superbadges|

### Example:

```data/trailhead_scores.tsv
@takahito0508	takahito0508	238	174,305	27	7	Ranger
Taro Yamada	005XXXXXXXXXXXXXXX	100	100,000	10	0	Mountaineer
```
