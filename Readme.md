## How to use
Just run run.sh, it would launch a docker with port 8088

## API

  ### Get /investments?date=2018-01-01

  return
  ```
  [
    {
      "company": "Meetly",
      "quantity": 1000,
      "cost": 1000
    },
    {
      "company": "IMIM",
      "quantity": 1000,
      "cost": 1000
    }
  ]
  ```


  ### Post /investments

  body
  ```
  {
    "company": "Meetly",
    "quantity": 1000,
    "cost": 1000,
    "creation_date": (optional)default value would be current date
  }
  ```

  return
  ```
  {
    "id": 1
    "company": "Meetly",
    "quantity": 100,
    "cost": 100,
    "creation_date": "2018-12-04"
  }
  ```

  ### Put /investments/{InvestmentId}

  body
  ```
  {
    "company": "Meetly",
    "quantity": 100,
    "cost": 100,
    "creation_date": "2018-11-11"
  }
  ```

  return
  ```
  {
    "id": 1
    "company": "Meetly",
    "quantity": 100,
    "cost": 100,
    "creation_date": "2018-12-04"
  }
  ```


