import mood_ring as mr


def test_ring_output_membership():
    mood_list = mr._default_mood_map.keys()
    mood_ring = mr.Ring()
    assert str(mood_ring) in mood_list
