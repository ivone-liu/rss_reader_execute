<?php
namespace app\api\validate;

use think\Validate;
/**
 * 验证登入信息
 */
class SignInValidate extends Validate
{
	
	protected $rule = [
        'email'         =>  'require',
        'password'      =>  'require',
    ];

    protected $message  =   [
        'email.require'      => '登入邮箱不能为空',
        'password.mobile'    => '登入密码不能为空',  
    ];
}