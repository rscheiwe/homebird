# HomeBird API

To run locally:

```angular2html
$ uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8002
```

**Note:** The data is generated at runtime if and only if no data is detected in a local `json` file.

To refresh data:
1) Delete `homebird.json`
2) Re-deploy (locally or via server) to refresh `homebird.json`

### URLs

Deployed at: [homebird.herokuapp.com](homebird.herokuapp.com)

Swagger Docs: [homebird.herokuapp.com/docs](homebird.herokuapp.com/docs)

### API Endpoints

#### GET
`official client only` [/homebird/homes](#get-all-homes-datajson) <br/>
`official client only` [/homebird/homes-ids](#get-all-homes-ids-datajson) <br/>
`official client only` [/homebird/homes/{home_id}](#get-home-by-id-datajson) <br/>


### To DO:
#### POST
`official client only` [/homebird/homes](#post-add-home-trialjson) <br/>
