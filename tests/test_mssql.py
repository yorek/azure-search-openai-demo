import json

import pytest
import pyodbc

from .mocks import MockAsyncPageIterator


@pytest.mark.asyncio
async def test_chathistory_newitem(auth_public_documents_client, monkeypatch):

    async def mock_upsert_item(cursor, item, **kwargs):
        assert item["id"] == "123"
        assert item["answers"] == [["This is a test message"]]
        assert item["entra_oid"] == "OID_X"
        assert item["title"] == "This is a test message"

    #monkeypatch.setattr(pyodbc.Cursor, "execute", mock_upsert_item)

    response = await auth_public_documents_client.post(
        "/chat_history/mssql",
        headers={"Authorization": "Bearer MockToken"},
        json={
            "id": "123",
            "answers": [["This is a test message"]],
        },
    )
    assert response.status_code == 201

