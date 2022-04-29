"""Test the csv upload"""

def test_csv(application, client):
    res = client.get("/songs/upload")
    print(res.data)
    assert res.status_code == 302
    upload_res = client.post("/songs/upload", data="/tests/csvs/music.csv", follow_redirects=True)
    assert upload_res.status_code == 200