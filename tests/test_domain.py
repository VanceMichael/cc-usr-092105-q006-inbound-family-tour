import unittest
from pathlib import Path
from src.domain import load_domain

class DomainTest(unittest.TestCase):
    def test_fixture_is_complete(self):
        value = load_domain(Path("fixtures/domain.json"))
        self.assertEqual(value["domain"], "inbound-family-tour")
        self.assertGreater(len(value["entities"]), 2)
        self.assertGreater(len(value["rules"]), 2)

    def test_core_entities_present(self):
        value = load_domain(Path("fixtures/domain.json"))
        entities = set(value["entities"])
        expected = {
            "询盘记录", "团组成员", "同行关系", "资料授权", "城市偏好",
            "行程版本", "报价方案", "翻译服务", "供应商确认", "地接确认",
            "入境便利信息", "费用分摊记录", "候补资源", "变更记录",
            "退款记录", "行程确认单",
        }
        self.assertTrue(expected.issubset(entities))

    def test_core_rules_present(self):
        value = load_domain(Path("fixtures/domain.json"))
        rules = value["rules"]
        keywords = ["费用分摊", "营销", "必需字段", "有效期", "候补",
                    "改线", "退款", "确认单", "提出方", "跨时区"]
        for word in keywords:
            self.assertTrue(any(word in rule for rule in rules), word)

if __name__ == "__main__":
    unittest.main()
