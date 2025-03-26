from pages.swag_labs import SwagLabs

def test_check_icon(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    assert demo_qa_page.exist_icon()
