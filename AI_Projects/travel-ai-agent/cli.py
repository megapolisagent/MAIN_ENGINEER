#!/usr/bin/env python3
import json
import argparse
from src.agent import TravelAgent


def main():
    parser = argparse.ArgumentParser(description='Travel-agent CLI (mock)')
    parser.add_argument('--city', '-c', required=True, help='City name')
    parser.add_argument('--days', '-d', type=int, default=1)
    parser.add_argument('--profile', '-p', default='all')
    parser.add_argument('--limit', '-l', type=int, default=10)
    parser.add_argument('--source', '-s', default='mock', help='Data source: mock or osm')
    args = parser.parse_args()

    agent = TravelAgent()
    items = agent.search(args.city, args.days, args.profile, args.limit, source=args.source)
    out = {"trip": f"{args.city}, {args.days} days", "items": items}
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
