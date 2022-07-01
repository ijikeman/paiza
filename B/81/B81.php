<?php
/**
 * Get 1 Line from STDIN
 *
 * @method get()
 * @return
 *   - string or FALSE
 */
class Stdin {
    function get() {
        if ($result = fgets(STDIN)) {
            $result = trim($result);
            return $result;
        }
        return FALSE;
    }
}

/** 
 * Get Multi Line from STDIN
 *
 * @method get()
 * @param int $max_num: 最大取得可能行
 * @return
 *   - array()
 */
class Stdins extends Stdin {
    function __construct($max_num) {
        $this->max_num = $max_num;
    }
    function get() {
        $list = array();
        for ($i=0; $i < $this->max_num; $i++) {
            $result = parent::get();
            if ($result == FALSE) {
                break;
            } else {
                array_push($list, $result);
            }
        }
        return $list;
    }
}
/**
 * Set Data of Paiza-format to Array
 *
 * @method setData()
 * @method getData()
 * @param int $max_num
 */
class PaizaData extends Stdins {
    function __construct() {
        $this->data = array();
    }
    function setData($max_num) {
        parent::__construct($max_num);
        $this->data[] = parent::get();
    }
    function getData($array_num) {
        return $this->data[$array_num];
    }
}

/**
 * 判定した数値を返す
 */
class JudgeB81
    $SCORE = 0;
    function judge($current_data, $before_data, $before_line_data) {
        $this->current_data = $current_data;
        $this->before_data = $before_data;
        $this->before_line_data = $before_line_data;
        return $SCORE;
    }


/**
 *  main
 */
$paiza = new PaizaData();
$paiza->setData(1); // get first line
list($tate_max, $yoko_max) = explode(' ', trim($paiza->getData(0)[0])); // parse First Line
$paiza->setData($tate_max); // データを設置
print_r($paiza->data);

/* データ分析開始 */


/*
foreach (explode(' ', trim($paiza->getData(0)[0])) as $i) { // parse First Line
    $paiza->setData($i);
    print_r($paiza->data);
}
// 条件
/* -- 全ての行で判定する
// 前がなしで次が. 0
// 前がなしで次が# +1
// 前が.で次が# +1
// 前が.で次が. 0
// 前が#で次が# 0
// 前が#で次が. +1

/* -- 最初の行と最後の行は判定する
// 最初/最終行.なら 0
// 最初/最終行#なら +1

/* -- 最初の行以外は判定する
// 前の行がなしで.0
// 前の行がなしで# +1
// 前の行が.で. 0
// 前の行が#で. +1
// 前の行が.で# +1
// 前の行が#で # 0

/* --判定条件終了 --

.##.
.##.
.##.
.##.
// 0211 4
// 0101 2
// 0101 2
// 0211 4
=12

..#.
..#.
###.
..#.
// 0021
// 0011
// 2101
// 1121
=14
?>
