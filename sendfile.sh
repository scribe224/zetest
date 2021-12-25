#!/bin/sh
curl -XPOST http://localhost:8000 -F "status=okcurl" -F "text=curlhello" -F "sourceimage=@/home/vittorio/ZeBrains/zetest/test.jpg"