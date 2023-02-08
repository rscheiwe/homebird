# HomeBird API

To run locally:

```angular2html
>> uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8002
```

### URLs

Deployed at: [homebird.herokuapp.com](homebird.herokuapp.com)

Swagger Docs: [homebird.herokuapp.com/docs](homebird.herokuapp.com/docs)

### API Endpoints

#### GET
`official client only` [/homebird/homes](#get-all-homes-datajson) <br/>
`official client only` [/homebird/homes-ids](#get-all-homes-ids-datajson) <br/>
`official client only` [/homebird/homes/{home_id}](#get-home-by-id-datajson) <br/>

#### POST
`official client only` [/homebird/homes](#post-add-home-trialjson) <br/>
