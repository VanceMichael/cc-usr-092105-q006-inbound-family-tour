import unittest
from pathlib import Path
from src.domain import load_domain

class DomainTest(unittest.TestCase):
    def setUp(self):
        self.value = load_domain(Path("fixtures/domain.json"))

    def test_fixture_is_complete(self):
        self.assertEqual(self.value["domain"], "inbound-family-tour")
        self.assertGreaterEqual(self.value["version"], 2)
        self.assertGreater(len(self.value["entities"]), 2)
        self.assertGreater(len(self.value["rules"]), 2)

    def test_core_entities_present(self):
        entities = set(self.value["entities"])
        for name in [
            "询盘",
            "团组成员",
            "同行关系",
            "证件资料与授权",
            "城市偏好",
            "报价方案（含版本与有效期）",
            "交通与住宿资源",
            "翻译服务",
            "供应商与地接确认",
            "入境便利信息",
            "行程版本",
            "费用分摊",
            "候补与替换记录",
            "退款记录",
            "调整记录（发起人、影响范围、费用差额）",
            "对外披露视图（最小化披露）",
        ]:
            self.assertIn(name, entities, f"缺少实体：{name}")

    def test_key_rules_present(self):
        rules = set(self.value["rules"])
        for keyword in [
            "费用分摊",
            "营销",
            "最小化披露",
            "有效期",
            "跨时区",
            "候补替换",
            "临时改线",
            "退款",
            "已确认的行程版本",
            "调整",
            "授权",
        ]:
            self.assertTrue(
                any(keyword in rule for rule in rules),
                f"缺少涉及「{keyword}」的规则",
            )

    def test_sample_reflects_scenario(self):
        sample = self.value["sample"]
        self.assertEqual(sample["group_size"], 8)
        self.assertEqual(sample["destination"], "重庆")
        self.assertEqual(sample["prior_destinations"], ["北京", "上海"])
        self.assertEqual(sample["language_need"], "阿拉伯语翻译")
        self.assertIn("travel_pattern", sample)

if __name__ == "__main__":
    unittest.main()
