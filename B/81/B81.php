<?php
class Stdin {
    function get() {
        if ($result = fgets(STDIN)) {
            $result = trim($result);
        }
        return $result;
    }
}

class Stdins extends Stdin {
    function __construct($max_num) {
        $this->max_num = $max_num; // 最大取得数を格納
        $this->list = array(); // 取得した値を格納

        for ($i=0; $i < $this->max_num; $i++) {
            $result = parent::get();
            if ($result == FALSE) {
                break;
            } else {
                array_push($this->list, $result);
            }
        }
    }
}

$first_line = new Stdins(1);
list($max_tate, $max_yoko) = explode(' ', $first_line->list[0]);

$data_master = new Stdins($max_tate);
print_r($data_master->list);

// 最上段/最下段 +1
// 一番左、一番右 +1
// 前が or 後ろが.なら +1
// #は1

?>
